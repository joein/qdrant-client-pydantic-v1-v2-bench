#!/bin/bash

set -e

source venv/bin/activate
echo 'Starting Qdrant container'
docker run --rm -d -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant:latest
pip3 install pydantic==1.10.8 -q
echo 'Running pydantic v1 (1.10.8)'
python3 -m run
pip3 install pydantic==2.1.1 -q
echo 'Running pydantic v2 (2.1.1)'
python3 -m run
echo 'Building plots'
python3 -m plots
echo 'Stopping Qdrant container'
docker stop qdrant
echo 'Done'
