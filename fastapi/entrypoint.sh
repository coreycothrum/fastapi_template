#!/usr/bin/env bash
set -eu

python /app/app/database/session.py

alembic upgrade head

python /app/app/main.py
