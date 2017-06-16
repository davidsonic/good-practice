import matplotlib.pyplot as plt
from fusion_test import get_gt, get_feat, get_pred_from_probs
from fusion_nets import  get_inception_feat
import numpy as np
from sklearn.metrics import confusion_matrix
from matplotlib.colors import LinearSegmentedColormap



def draw_conf(name, conf_arr):
    conf_arr = np.array(conf_arr[:20, :20])
    xtick_pos = [0, 4, 9, 14, 19]
    xtick_labels = [1, 5, 10, 15, 20]

    norm_conf = []
    for i in conf_arr:
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/float(a))
        norm_conf.append(tmp_arr)

    fig = plt.figure(figsize=(6, 4))
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)

    # custom cm
    colors = [(230./255, 245./255, 230./255), (70./255, 120./255, 45./255)]
    cm = LinearSegmentedColormap.from_list('my_cm', colors, N=256)


    res = ax.imshow(np.array(norm_conf), cmap=cm, interpolation='nearest')
    plt.xticks(np.array(xtick_pos, dtype=float), xtick_labels)
    plt.yticks(np.array(xtick_pos, dtype=float), xtick_labels)

    # for sub-confusion_matrix
    # plt.xticks([0] + range(4, 249, 5) + [248])
    # plt.yticks([0] + range(4, 249, 5) + [248])
    # ax.set_xticklabels([1] + range(5, 249, 5) + [249])
    # ax.set_yticklabels([1] + range(5, 249, 5) + [249])

    # cb = fig.colorbar(res)
    plt.tight_layout()
    plt.savefig('./'+name+'.png', bbox_inches='tight')

    # plt.show()


def draw_whole(name, conf_arr):
    xtick_pos = [0] + range(9, 249, 10) + [248]
    xtick_labels = [1] + range(10, 250, 10) + [249]

    norm_conf = []
    for i in conf_arr:
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/float(a))
        norm_conf.append(tmp_arr)

    fig = plt.figure(figsize=(14.5, 12))
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)

    # custom cm
    colors = [(230./255, 245./255, 230./255), (70./255, 120./255, 45./255)]
    cm = LinearSegmentedColormap.from_list('my_cm', colors, N=256)

    res = ax.imshow(np.array(norm_conf), cmap=cm, interpolation='nearest')
    plt.xticks(np.array(xtick_pos, dtype=float), xtick_labels, rotation='vertical', size=12)
    plt.yticks(np.array(xtick_pos, dtype=float), xtick_labels, size=12)

    cb = fig.colorbar(res)
    plt.tight_layout()
    plt.savefig('./'+name+'.png', bbox_inches='tight')

    # plt.show()


def main():
    gt_labels = get_gt()
    incep_1,incep_2, incep_rgb, incep_flow = get_inception_feat()
    # c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs = get_feat()

    conf_matrix_rgb = confusion_matrix(gt_labels, get_pred_from_probs(incep_rgb))
    conf_matrix_rgb_flow = confusion_matrix(gt_labels, get_pred_from_probs(incep_flow))

    # conf_matrix_fusion = confusion_matrix(gt_labels, get_pred_from_probs(incep_rgb + incep_flow*2))
    # conf_matrix_c3d_depth = confusion_matrix(gt_labels, get_pred_from_probs(c3d_depth_probs))
    # conf_matrix_c3d_sal = confusion_matrix(gt_labels, get_pred_from_probs(c3d_sal_probs))
    # conf_matrix_c3d_rgb = confusion_matrix(gt_labels, get_pred_from_probs(c3d_rgb_probs))
    # conf_matrix_c3d_fusion = confusion_matrix(gt_labels, get_pred_from_probs(c3d_depth_probs*2 + c3d_sal_probs))
    # conf_matrix_overall_fusion = confusion_matrix(gt_labels, overall_fusion_preds)


    draw_conf('2SCVN_Depth', conf_matrix_rgb)
    draw_conf('2SCVN_Depth_flow', conf_matrix_rgb_flow)
    # draw_conf('2SCVN_fusion', conf_matrix_fusion)
    # draw_conf('3DDSN_depth', conf_matrix_c3d_depth)
    # draw_conf('3DDSN_sal', conf_matrix_c3d_sal)
    # draw_conf('3DDSN_fusion', conf_matrix_c3d_fusion)
    # draw_conf('3DDSN_rgb', conf_matrix_c3d_rgb)
    # draw_conf('overall_fusion', conf_matrix_overall_fusion)


    draw_whole('2SCVN_Depth_249', conf_matrix_rgb)
    draw_whole('2SCVN_Depth_flow_249', conf_matrix_rgb_flow)
    # draw_whole('2SCVN_fusion_249', conf_matrix_fusion)
    # draw_whole('3DDSN_depth_249', conf_matrix_c3d_depth)
    # draw_whole('3DDSN_sal_249', conf_matrix_c3d_sal)
    # draw_whole('3DDSN_fusion_249', conf_matrix_c3d_fusion)
    # draw_whole('overall_fusion_249', conf_matrix_overall_fusion)
    # draw_whole('3DDSN_rgb_249', conf_matrix_c3d_rgb)

if __name__ == '__main__':
    main()

# class_acc = np.array([0.] * 249)
# class_count = np.array([0.] * 249)
# for i, gt_label in enumerate(gt_labels):
#     class_count[gt_label] += 1
#     if gt_label == preds[i]:
#         class_acc[gt_label] += 1
# plt.figure(figsize=(16, 2))
# plt.bar(range(249), (class_acc/class_count), color=(240.0/255.0,28/255.0,1/255.0), width=1)
# plt.xticks(np.array(range(0, 250, 5), dtype=float) + 0.5, range(0, 250, 5), rotation='vertical', size=8)
# plt.yticks(size=8)
# plt.ylabel('Accuracy')
# plt.xlim([0, 249])
# plt.ylim([0, 1])
# plt.tight_layout()
#
# ax = plt.gca()
# ax.set_yticks(np.linspace(0.5, 1.0, 6).tolist()+[0.95], minor=False)
# ax.set_yticks([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0], minor=False)
# ax.set_yticks([0.6, 0.9, 0.95], minor=True)
# ax.grid(which='minor', alpha=0.8)
# plt.grid()
# plt.savefig('/data4/szhou/figures/huda_test/huda_class_acc.png', bbox_inches='tight')
