import fusion_test as c3d_fusion
import numpy as np


def get_inception_feat(score_file):
    incep_scores = np.load(score_file)
    # incep_rgb = []
    # incep_flow = []
    # for video_score in incep_scores[0]:
    #     prob = np.zeros(249, dtype=float)
    #     prob[0:248] = video_score
    #
    #     # prob[0:248] = c3d_fusion.softmax(video_score)
    #     incep_rgb.append(prob)
    # for video_score in incep_scores[1]:
    #     prob = np.zeros(249, dtype=float)
    #     # prob[0:248] = c3d_fusion.softmax(video_score)
    #     prob[0:248] = video_score
    #     incep_flow.append(prob)
    return np.array(incep_scores[0]), np.array(incep_scores[1])


def find_wrong(gt_labels):
    pred_labels = predictions()
    for i in range(4000, len(gt_labels)):
        if gt_labels[i] != pred_labels[i]:
            print gt_labels[i]+1, i
        if i > 4100:
            break

def sep(gt_labels, **kwds):
    for key, probs in kwds.items():
        pred_labels = c3d_fusion.get_pred_from_probs(probs)
        print '%s Acc: %f' % (key, c3d_fusion.cal_accuracy(pred_labels, gt_labels))


def write_prediction_file(pred_result, filename):
    out = open(filename, 'w')
    with open('test_list.txt') as test_name_list_f:
        gt_names = test_name_list_f.readlines()
    assert len(gt_names) == len(pred_result)
    for i, line in enumerate(gt_names):
        m_name, k_name = line.split()
        label = pred_result[i] + 1
        out.write('%s %s %d\n' % (m_name, k_name, label))
    out.close()


def two_score_fusion(score_a, score_b, gt_labels):
    weight_ratios = np.array(range(1, 11), dtype=float)
    total = len(gt_labels)
    acc_map = np.zeros((11, 11), dtype=float)
    for weight_a in weight_ratios:
        for weight_b in weight_ratios:
            acc = 0.
            for i in range(total):
                pred = (score_a[i] * weight_a + score_b[i] * weight_b).argmax()
                if pred == gt_labels[i]:
                    acc += 1
            if acc / total < 0.963:
                print weight_a, weight_b, acc / total
            acc_map[weight_a][weight_b] = acc / total
    weight_a, weight_b = np.where(acc_map == np.max(acc_map))
    print weight_a, weight_b
    return acc_map


def four_score_fusion(score_a, score_b, score_c, score_d, gt_labels):
    weight_ratios = np.array(range(1, 6), dtype=float)
    total = len(gt_labels)
    acc_map = np.zeros((6, 6, 6, 6), dtype=float)
    for weight_a in weight_ratios:
        for weight_b in weight_ratios:
            for weight_c in weight_ratios:
                for weight_d in weight_ratios:
                                acc = 0.
                                for i in range(total):
                                    pred = (score_a[i] * weight_a + score_b[i] * weight_b +
                                            score_c[i] * weight_c + score_d[i] * weight_d).argmax()
                                    if pred == gt_labels[i]:
                                        acc += 1
                                # if weight_a < 7 and weight_b < 7 and weight_c < 7 and weight_d < 7:
                                print weight_a, weight_b, weight_c, weight_d, acc / total

                                acc_map[weight_a][weight_b][weight_c][weight_d] = acc / total
    weight_a, weight_b, weight_c, weight_d = np.where(acc_map == np.max(acc_map))
    print weight_a, weight_b, weight_c, weight_d
    return acc_map


def predictions():
    depth_probs, sal_probs, rgb_probs= c3d_fusion.get_feat()
    incep_rgb, incep_flow = get_inception_feat('gesture_rgb_final.npy')
    # print 'incep_rgb', incep_rgb.shape
    # print 'incep_flow*4', (incep_flow*4).shape
    # print 'depth_probs*2', (depth_probs*2).shape
    # print 'sal_probs', sal_probs.shape
    return c3d_fusion.get_pred_from_probs(incep_rgb*2 + incep_flow*4 + depth_probs*2 + sal_probs)


if __name__ == '__main__':

    gt_labels = c3d_fusion.get_gt()
    # incep_rgb, incep_flow = get_inception_feat('gesture_rgb_final.npy')
    #
    c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs = c3d_fusion.get_feat()
    #
    # sep(gt_labels,
    #     incep_rgb=incep_rgb, incep_rgb_flow=incep_flow, incep_rgb_rgb_flow=incep_rgb+incep_flow*2,
    #     c3d_depth=c3d_depth_probs, c3d_sal=c3d_sal_probs, c3d_rgb=c3d_rgb_probs)
    # find_wrong(gt_labels)
    # two_score_fusion(incep_rgb, incep_flow, gt_labels)
    # four_score_fusion(incep_rgb, incep_flow, c3d_depth_probs, c3d_sal_probs, gt_labels)
    # fusion_rgb_flow(incep_rgb, incep_flow, gt_labels)
    # fusion_nets(c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs, incep_rgb, incep_flow, gt_labels)
    # c3d_rgb_only = fusion_result([
    #                                   # (c3d_depth_probs, 2),
    #                                   # (c3d_sal_probs, 1),
    #                                   (c3d_rgb_probs, 1),
    #                                   # (incep_rgb, 2),
    #                                   # (incep_flow, 4)
    #                                  ])
    # write_prediction_file(c3d_rgb_only, 'c3d_rgb_only.txt')
    # print 'c3d_rgb_only', c3d_fusion.cal_accuracy(c3d_rgb_only, gt_labels)

    incep_rgb, incep_rgb_flow = get_inception_feat('gesture_rgb_final.npy')
    # sep(gt_labels, incep_depth=incep_depth, incep_depth_flow=incep_depth_flow)
    four_score_fusion(c3d_depth_probs,c3d_sal_probs,incep_rgb, incep_rgb_flow,gt_labels)
