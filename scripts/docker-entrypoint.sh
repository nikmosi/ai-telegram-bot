#!/usr/bin/env bash


cd src && alembic upgrade head; cd ..
python src/main.py
