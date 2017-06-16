import argparse
import os
import sys

sys.path.append('.')
from pyActionRecog import parse_directory, build_split_list, build_gesture_train, build_gesture_test
from pyActionRecog import parse_split_file

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=str, choices=['ucf101', 'hmdb51','gesture'])
parser.add_argument('frame_path', type=str, help="root directory holding the frames")
parser.add_argument('--rgb_prefix', type=str, help="prefix of RGB frames", default='img_')
parser.add_argument('--flow_x_prefix', type=str, help="prefix of x direction flow images", default='flow_x')
parser.add_argument('--flow_y_prefix', type=str, help="prefix of y direction flow images", default='flow_y')
parser.add_argument('--num_split', type=int, default=1)
parser.add_argument('--out_list_path', type=str, default='data/')
parser.add_argument('--shuffle', action='store_true', default=True)

args = parser.parse_args()

dataset = args.dataset
frame_path = args.frame_path
rgb_p = args.rgb_prefix
flow_x_p = args.flow_x_prefix
flow_y_p = args.flow_y_prefix
num_split = args.num_split
out_path = args.out_list_path
shuffle = args.shuffle


# operation
print 'processing dataset {}'.format(dataset)
split_tp = parse_split_file(dataset)
f_info_train = parse_directory('../data/iso_train_depth/', rgb_p, flow_x_p, flow_y_p)
f_info_test = parse_directory('../data/iso_test_depth/', rgb_p, flow_x_p, flow_y_p)

print 'writting list files for training/testing'
out_path='/data4/jiali/good-practice/data/'

# got only one split
train_lists = build_gesture_train(split_tp[0][0],f_info_train, shuffle)
test_lists =  build_gesture_test(split_tp[0][1], f_info_test, shuffle)

open(os.path.join(out_path, '{}_depth_train_split_{}.txt'.format(dataset, 1)), 'w').writelines(train_lists[0])
open(os.path.join(out_path, '{}_depth_val_split_{}.txt'.format(dataset, 1)), 'w').writelines(test_lists[0])
open(os.path.join(out_path, '{}_depth_flow_train_split_{}.txt'.format(dataset, 1)), 'w').writelines(train_lists[1])
open(os.path.join(out_path, '{}_depth_flow_val_split_{}.txt'.format(dataset, 1)), 'w').writelines(test_lists[1])
