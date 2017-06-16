import sys
import re
from matplotlib import pyplot as plt
import numpy as np

train_pattern = re.compile('Iteration (\d*), loss = ([-+]?[0-9]*\.?[0-9]+)')
# I0309 15:59:47.188685 21484 solver.cpp:337] Iteration 11000, Testing net (#0)
test_i_pattern = re.compile('Iteration (\d+), Testing net')
# :404]     Test net output #0: loss = 1.13276 (* 1 = 1.13276 loss)
test_l_pattern = re.compile('Test net output #[01]: loss = ([-+]?[0-9]*\.?[0-9]+) \(')
# Test net output #0: accuracy = 0.66875
test_acc_pattern = re.compile('Test net output #0: accuracy = ([-+]?[0-9]*\.?[0-9]+)')


def get_loss(log_path):
    log_file = open(log_path, 'r')
    test_i = []
    test_l = []
    test_acc = []
    train_i = []
    train_loss = []

    loss_max = 0
    loss_max_sec = 0
    highest_acc = 0

    for line in log_file:
        t = test_i_pattern.search(line)
        if t:
            i = int(t.group(1))
            test_i.append(i)
            continue
        tl = test_l_pattern.search(line)
        if tl:
            l = float(tl.group(1))
            loss = l
            if loss > loss_max:
                loss_max = loss
            if loss_max_sec < loss < loss_max:
                loss_max_sec = loss
            test_l.append(l)
            continue
        # tacc = test_acc_pattern.search(line)
        # if tacc:
        #     acc = float(tacc.group(1))
        #     test_acc.append(acc)
        #     if acc > highest_acc:
        #         highest_acc = acc
        #     continue
        g = train_pattern.search(line)
        if g:
            # print g.group(1), g.group(2)
            i = int(g.group(1))
            loss = float(g.group(2))
            if loss > loss_max:
                loss_max = loss
            if loss_max_sec < loss < loss_max:
                loss_max_sec = loss
            train_i.append(i)
            train_loss.append(loss)
            continue
    return train_i, train_loss, test_i, test_l


def main():
    models = {'without_dropout': 'no_dropout.log',
              'dropout 0.5': 'dropout_0.5.log',
              'dropout 0.6': 'dropout_0.6.log',
              'dropout 0.7': 'dropout_0.7.log',
              'dropout 0.8': 'dropout_0.8.log',
              'dropout 0.9': 'dropout_0.9.log',
              }
    model_name_in_order = ['without_dropout', 'dropout 0.5', 'dropout 0.6', 'dropout 0.7', 'dropout 0.8', 'dropout 0.9']
    for model_name in model_name_in_order:
        log_name = models[model_name]
        train_i, train_l, test_i, test_l = get_loss('list_files/dropout/'+log_name)
        plt.plot(test_i, test_l, label=model_name)
    plt.xlim([0, 4000])
    plt.legend()
    plt.ylabel('Test loss')
    plt.xlabel('Iterations')
    plt.savefig('/data4/szhou/figures/isogd_incep_RGB_dropout_test_loss.png')
    plt.show()

    for model_name in model_name_in_order:
        log_name = models[model_name]
        train_i, train_l, test_i, test_l = get_loss('list_files/dropout/'+log_name)
        plt.plot(train_i, train_l, label=model_name)
    plt.xlim([0, 4000])
    plt.legend()
    plt.ylabel('Train loss')
    plt.xlabel('Iterations')
    plt.savefig('/data4/szhou/figures/isogd_incep_RGB_dropout_train_loss.png')
    plt.show()

main()
