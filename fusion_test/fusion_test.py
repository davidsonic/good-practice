import csv
import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def get_feat():
    depth_probs = []
    with open('depth_fc8.csv', 'r') as depth_csv:
        depth_reader = csv.reader(depth_csv)
        for video_id, row in enumerate(depth_reader):
            feats = map(float, row)
            # prob = softmax(feats)
            prob = np.array(feats)
            depth_probs.append(prob)
    sal_probs = []
    with open('sal_fc8.csv', 'r') as sal_csv:
        sal_reader = csv.reader(sal_csv)
        for video_id, row in enumerate(sal_reader):
            feats = map(float, row)
            # prob = softmax(feats)
            prob = np.array(feats)
            sal_probs.append(prob)
    rgb_probs = []
    with open('rgb_fc8.csv', 'r') as rgb_csv:
        rgb_reader = csv.reader(rgb_csv)
        for video_id, row in enumerate(rgb_reader):
            feats = map(float, row)
            prob = np.array(feats)
            # prob = softmax(feats)
            rgb_probs.append(prob)
    return depth_probs, sal_probs, rgb_probs


def get_gt():
    with open('test_ground_truth.txt', 'r') as gt_f:
        lines = gt_f.readlines()

    gt_labels = []
    for line in lines:
        video_id, label = line.split()
        label = int(label) - 1
        gt_labels.append(label)
    return gt_labels


def get_pred_from_probs(probs):
    pred = []
    for prob in probs:
        label = prob.argmax()
        pred.append(label)
    return pred


def cal_accuracy(labels, gt):
    total = len(gt)
    acc = 0
    for i in range(total):
        if labels[i] == gt[i]:
            acc += 1
    return acc * 1.0 / total


def fusion(depth, sal, gt_labels):
    weight_ratios = []
    tmp = np.array(range(1, 11), dtype=float)
    weight_ratios.extend(tmp)
    weight_ratios.extend(1 / np.array(tmp, dtype=float))

    total = len(gt_labels)
    accs = []
    weights = []
    for weight in weight_ratios:
        acc = 0.
        for i in range(total):
            pred = (depth[i] * weight + sal[i]).argmax()
            if pred == gt_labels[i]:
                acc += 1
        # print weight, acc / total
        accs.append(acc / total)
        weights.append(weight)


    return max(accs), weights[np.array(accs).argmax()], accs,weights


def fusion_with_rgb(depth, sal, rgb, gt_labels):
    weight_ratios = []
    tmp = np.array(range(1, 11), dtype=float)
    weight_ratios.extend(tmp)
    weight_ratios.extend(1 / np.array(tmp, dtype=float))
    total = len(gt_labels)

    for weight in weight_ratios:
        acc = 0.
        for i in range(total):
            pred = (rgb[i] * weight + 2 * depth[i] + sal[i]).argmax()
            if pred == gt_labels[i]:
                acc += 1
        print weight, acc / total



def get_ratio_list():
    weight_ratios = []
    tmp = np.array(range(1, 11), dtype=float)
    weight_ratios.extend(tmp)
    weight_ratios.extend(1 / np.array(tmp, dtype=float))
    return weight_ratios


def sep(depth_probs, sal_probs, rgb_probs, gt_labels):
    depth_labels = get_pred_from_probs(depth_probs)
    sal_labels = get_pred_from_probs(sal_probs)
    rgb_labels = get_pred_from_probs(rgb_probs)

    print '%s Acc: %f' % ('depth', cal_accuracy(depth_labels, gt_labels))
    print '%s Acc: %f' % ('sal', cal_accuracy(sal_labels, gt_labels))
    print '%s Acc: %f' % ('rgb', cal_accuracy(rgb_labels, gt_labels))


def get_prediction(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    labels = []
    for line in lines:
        label = line.strip().split(' ')[-1]
        label = int(label) - 1
        labels.append(label)
    return labels


def get_valid_gt(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    labels = []
    for line in lines:
        label = line.strip().split(' ')[-1]
        label = int(label) - 1
        labels.append(label)
    return labels



if __name__ == '__main__':
    # depth_probs, sal_probs, rgb_probs = get_feat()
    # gt_labels = get_gt()
    # sep(depth_probs, sal_probs, rgb_probs, gt_labels)

    # fusion_with_rgb(depth_probs, sal_probs, rgb_probs, gt_labels)
    # acc,weight,accs,weights=fusion(rgb_probs, depth_probs, gt_labels)
    # print 'highest weight:{}, acc:{}, modality:{}/{}'.format(weight,acc,'rgb','depth')


    prob=get_prediction('3DDSN_valid_prediction.txt')
    gt_labels=get_valid_gt('valid_list_with_label.txt')
    print cal_accuracy(prob,gt_labels)