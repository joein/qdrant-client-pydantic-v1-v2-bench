#!/bin/bash

set -e

echo 'Creating venv'
python3 -m venv venv
source venv/bin/activate
echo 'Installing dependencies'
pip3 install -U pip seaborn
pip3 install git+https://github.com/qdrant/qdrant-client.git@master
wget https://raw.githubusercontent.com/h4pZ/rose-pine-matplotlib/main/themes/rose-pine-moon.mplstyle -P styles
mkdir results
