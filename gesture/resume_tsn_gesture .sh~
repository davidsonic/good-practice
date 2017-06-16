#!/usr/bin/env bash

DATASET=$1
MODALITY=$2

TOOLS=lib/caffe-action/build/install/bin
LOG_FILE=logs/gesture_depth_resume.log
N_GPU=2
MPI_BIN_DIR= #/usr/local/openmpi/bin/


echo "logging to ${LOG_FILE}"

mpirun -np $N_GPU \
$TOOLS/caffe train --solver=models/${DATASET}_depth/tsn_bn_inception_${MODALITY}_solver.prototxt  \
   --snapshot=models/${DATASET}_depth_model/gesture_tsn_rgb_bn_inception_iter_3000.solverstate 2>&1 | tee ${LOG_FILE}
