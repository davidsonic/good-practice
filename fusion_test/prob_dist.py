import fusion_nets
from fusion_test import softmax, get_gt
import matplotlib.pyplot as plt
import numpy as np

from draw_dataset_stats import get_labels


def draw_bins(feat, title, ground_truth):
    rgb_probs = softmax(feat)
    tops = rgb_probs.argsort()[::-1][:5] + 1
    fig = plt.figure(num=None, figsize=(8, 1.2))
    ax = fig.add_subplot(111)

    prob = np.zeros((10, 249))
    for i in range(10):
        prob[i, ...] = rgb_probs
    plt.contourf(prob, )
    # ax.bar(range(249), rgb_probs, width=1)
    # ax.text(230, 0.95, ground_truth, bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})
    # ax.text(230, 0.65, text, bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 10})
    ax.get_yaxis().set_visible(False)
    # plt.title(title)
    labels = get_labels()
    plt.xticks(np.array(range(len(labels)), dtype=float) + 0.5, labels, rotation='vertical', size='small')
    plt.ylim([0, 1])
    plt.tight_layout()
    top_pred = '_'.join(map(str, tops))
    name = '%s_GT_%s_PRED_%s.png' % (title, ground_truth, top_pred)
    print name
    plt.savefig('/data4/szhou/figures/'+name)
    plt.show()


def main():
    ince_rgb, ince_flow = fusion_nets.get_inception_feat()
    gt_labels = get_gt()

    sample_list = [883, 1055, 1204, 1668, 2528, 4368]
    for i in sample_list:
        i = i -1
        draw_bins(ince_rgb[i], str(i+1), gt_labels[i] + 1)

main()
