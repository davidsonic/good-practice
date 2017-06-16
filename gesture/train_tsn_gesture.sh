#!/usr/bin/env bash

DATASET=$1
MODALITY=$2

TOOLS=lib/caffe-action/build/install/bin
LOG_FILE=logs/${DATASET}_${MODALITY}.log
N_GPU=2
MPI_BIN_DIR= /usr/local/openmpi/bin/


echo "logging to ${LOG_FILE}"

mpirun -np $N_GPU \
$TOOLS/caffe train --solver=models/${DATASET}/tsn_bn_inception_${MODALITY}_solver.prototxt \
   --weights=models/bn_inception_rgb_init.caffemodel 2>&1 | tee ${LOG_FILE}
