#!/usr/bin/env bash


echo "start migrations"
cd src && alembic upgrade head; cd ..
echo "end migrations"
echo "start app"
python src/main.py
echo "end app"
