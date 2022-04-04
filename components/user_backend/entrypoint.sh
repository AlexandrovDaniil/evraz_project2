#!/usr/bin/env bash

gunicorn -b 127.0.0.1:8002 user.composites.user_api:app --reload


