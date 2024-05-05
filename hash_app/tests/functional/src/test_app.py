from contextlib import nullcontext as does_not_raise

import aiohttp
import pytest

from tests.functional.utils.client_helpers import make_get_request, make_post_request


@pytest.mark.parametrize(
    "expected_answer, expectation",
    [
        (
                {
                    "status": 200,
                },
                does_not_raise(),
        )
    ],
)
@pytest.mark.asyncio
async def test_healthcheck(
        aiohttp_session,
        url_hash_service,
        expected_answer,
        expectation,
):
    url = url_hash_service + "/healthcheck"
    with expectation:
        response, response_status = await make_get_request(aiohttp_session, url, {})
        assert expected_answer["status"] == response_status


@pytest.mark.parametrize(
    "body, expected_answer, expectation",
    [
        (
                {
                    "string": "may",
                },
                {
                    "status": 200,
                    "hash_string": "ee4d988c65de860fabbfbcd27f73d50bbebe3fba37fe419284f4811389c30bdc",
                },
                does_not_raise(),
        ),
        (
                {
                    "wrong_string": "may",
                },
                {
                    "status": 400,
                },
                pytest.raises(aiohttp.ClientResponseError),
        ),
        (
                {
                    "wrong_string": 123,
                },
                {
                    "status": 400,
                },
                pytest.raises(aiohttp.ClientResponseError),
        ),
        (
                {},
                {
                    "status": 400,
                },
                pytest.raises(aiohttp.ClientResponseError),
        )
    ],
)
@pytest.mark.asyncio
async def test_hash(
        aiohttp_session,
        url_hash_service,
        body,
        expected_answer,
        expectation,
):
    url = url_hash_service + "/hash"
    with expectation:
        response, response_status = await make_post_request(aiohttp_session, url, body)
        assert expected_answer["status"] == response_status
        assert expected_answer["hash_string"] == response["hash_string"]
