import fusion_test as c3d_fusion
import numpy as np


def get_inception_feat():
    incep_s = np.load('../scores/gesture_depth_flow/gesture_depth_flow_new_mean.npy')
    incep_scores = np.load('gesture_rgb_final.npy')


    # incep_rgb = []
    # incep_flow = []
    # for video_score in incep_scores[0]:
    #     prob = np.zeros(249, dtype=float)
    #     prob[0:248] = video_score[0:248]
    #
    #     # prob[0:248] = c3d_fusion.softmax(video_score)
    #     incep_rgb.append(prob)
    # for video_score in incep_scores[1]:
    #     prob = np.zeros(249, dtype=float)
    #     # prob[0:248] = c3d_fusion.softmax(video_score)
    #     prob[0:248] = video_score[0:248]
    #     incep_flow.append(prob)
    # return incep_rgb, incep_flow

    return np.array(incep_scores[0]),np.array(incep_scores[1]), np.array(incep_s[0]),np.array(incep_s[1])


def sep(rgb_probs, flow_probs, gt_labels):
    rgb_labels = c3d_fusion.get_pred_from_probs(rgb_probs)
    flow_labels = c3d_fusion.get_pred_from_probs(flow_probs)

    print '%s Acc: %f' % ('2scvn-rgb', c3d_fusion.cal_accuracy(rgb_labels, gt_labels))
    print '%s Acc: %f' % ('2scvn-flow', c3d_fusion.cal_accuracy(flow_labels, gt_labels))



def sep3d(rgb,flow,sal,gt_labels):
    rgb_label=c3d_fusion.get_pred_from_probs(rgb)
    flow_label=c3d_fusion.get_pred_from_probs(flow)
    sal_label=c3d_fusion.get_pred_from_probs(sal)

    print '%s ACC: %f' % ('c3d-rgb',c3d_fusion.cal_accuracy(rgb_label,gt_labels))
    print '%s ACC: %f' % ('c3d-depth', c3d_fusion.cal_accuracy(flow_label, gt_labels))
    print '%s ACC: %f' % ('c3d-sal', c3d_fusion.cal_accuracy(sal_label, gt_labels))


def fusion_rgb_flow(incep_rgb, incep_flow, gt_labels):
    weight_ratios = []
    tmp = np.array(range(1, 11), dtype=float)
    weight_ratios.extend(tmp)
    weight_ratios.extend(1 / np.array(tmp, dtype=float))

    accs=[]
    total = len(gt_labels)
    for weight in weight_ratios:
        acc = 0.
        for i in range(total):
            pred = (incep_rgb[i] * weight + incep_flow[i]).argmax()
            if pred == gt_labels[i]:
                acc += 1
        # print weight, acc / total\
        accs.append(acc/total)
    return max(accs)


def fusion_nets(c3d_d, c3d_s, c3d_r, incep_r, incep_f, incep_d,incep_d_f, gt_labels):
    ratios = c3d_fusion.get_ratio_list()
    total = len(gt_labels)
    for weight in ratios:
        acc = 0.
        for i in range(total):
            pred = ((incep_r[i] + incep_f[i] * 2) * weight + ((c3d_d[i] * 2 + c3d_s[i])+ (incep_d[i]+incep_d_f[i]))).argmax()

            # (incep_r[i] + incep_f[i] * 2) * weight + (c3d_d[i] * 2 + c3d_s[i])).argmax()
            # pred = (incep_rgb[i] * weight + incep_flow[i]).argmax()
            if pred == gt_labels[i]:
                acc += 1
        print weight, acc / total


def fusion_prob(c3d_d, c3d_s, c3d_r, incep_r, incep_f):
    predictions = []
    for i in range(len(c3d_d)):
        pred = (2*incep_r[i] + 4*incep_f[i] + 2*c3d_d[i] + 0*c3d_s[i]).argmax() #0 to exclude sal
        predictions.append(pred)
    return predictions


def fusion_depth(c3d_d,incep_d, incep_d_f, gt_labels):
    prediction =[]
    ratios=c3d_fusion.get_ratio_list()

    total = len(gt_labels)
    for weight in ratios:
        acc = 0.
        for i in range(total):
            pred = ((incep_d[i] + incep_d_f[i]) *weight + c3d_d[i]).argmax()
            prediction.append(pred)
            if pred == gt_labels[i]:
                acc += 1
        # print weight, acc / total
    return prediction


def fusion_acc(gt, pred):
    acc = 0.
    total = len(gt)
    for i in range(len(gt)):
        if pred[i] == gt[i]:
            acc += 1
    return acc / total


if __name__ == '__main__':
    incep_rgb, incep_flow, incep_d, incep_d_f = get_inception_feat()
    gt_labels = c3d_fusion.get_gt()

    c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs = c3d_fusion.get_feat()

    sep(incep_rgb, incep_flow, gt_labels)
    sep3d(c3d_rgb_probs, c3d_depth_probs, c3d_sal_probs,gt_labels)

    # d_prediction=fusion_depth(c3d_depth_probs,incep_d, incep_d_f,gt_labels)

    # fusion_rgb_flow(incep_rgb, incep_flow, gt_labels)
    # fusion_nets(c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs, incep_rgb, incep_flow, incep_d,incep_d_f, gt_labels)
    # print fusion_acc(gt_labels, fusion_prob(c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs, incep_rgb, incep_flow))


    # 3DDSN fusion
    c3d_fusion_acc=c3d_fusion.fusion(c3d_depth_probs,c3d_sal_probs,gt_labels)[0]
    print '%s ACC: %f' % ('3DDSN-fusion', c3d_fusion_acc)


    #2SCVN fusion
    scvn_fusion=fusion_rgb_flow(incep_rgb,incep_flow,gt_labels)
    print '%s ACC: %f' % ('2SCVN-fusion', scvn_fusion)


    #2SCVN-3DDSN fusion
    print '%s ACC: %.4f' %('2SCVN-3DDSN',fusion_acc(gt_labels, fusion_prob(c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs, incep_rgb, incep_flow)))


    #final prediction result
    result = fusion_prob(c3d_depth_probs, c3d_sal_probs, c3d_rgb_probs, incep_rgb, incep_flow)
    count=0
    with open('predict_result.txt','w') as fw:
        with open('test_ground_truth.txt') as f:
            lines=f.readlines()
            for line in lines:
                file=line.split(' ')[0]
                fw.write(file+' '+str(result[count]+1)+'\n')
                count+=1



