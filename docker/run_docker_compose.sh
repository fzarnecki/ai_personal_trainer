#!/bin/bash

export COMPOSE_PROJECT_NAME="aipt"
export DEMO_PORT=8501
export DATA_DIR="./data/"

docker compose rm -fs

echo "COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}" > .env
echo "DEMO_PORT=${DEMO_PORT}" >> .env
echo "DATA_DIR=${DATA_DIR}" >> .env

docker compose -f docker_compose.yml --env-file .env up --build -d