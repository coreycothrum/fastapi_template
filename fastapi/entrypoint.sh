#!/usr/bin/env bash
set -eu

python /app/app/database/session.py

python /app/app/main.py
