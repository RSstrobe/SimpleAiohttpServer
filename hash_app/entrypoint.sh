#!/bin/sh
python cli.py --host 0.0.0.0 --port $APP_PORT
exec "$@"
