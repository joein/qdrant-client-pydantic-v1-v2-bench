#!/bin/bash

set -e

echo 'Creating venv'
python3 -m venv venv
source venv/bin/activate
echo 'Installing dependencies'
pip3 install -U pip seaborn
pip3 install qdrant-client==1.3.2
mkdir results
