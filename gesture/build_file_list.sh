#!/usr/bin/env bash

DATASET=$1
FRAME_PATH=$2

python gesture/build_file_list.py ${DATASET} ${FRAME_PATH} --shuffle