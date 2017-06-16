import numpy as np
import matplotlib.pyplot as plt
import os


def get_labels():
    labels = []
    for i in range(1, 250):
        if i % 10 == 0:
            labels.append(str(i))
        elif i == 1 or i == 249:
            labels.append(str(i))
        else:
            labels.append('')
    return labels


def get_isogd_stats():
    sub_sets = ['train', 'valid', 'test']
    whole_list = []
    for subset in sub_sets[:1]:
        with open(os.path.join('list_files', 'iso_'+subset+'.list')) as list_f:
            whole_list.extend(list_f.readlines())



    label_count = []
    for i in range(1, 250):
        label_count.append(0)

    for line in whole_list:
        _, _, label = line.split()
        label = int(label) - 1
        label_count[label] += 1
    return get_labels(), label_count


def draw_dataset_stats(labels, label_count):
    fig = plt.figure(num=None, dpi=200)
    plt.bar(range(len(labels)), label_count, color=(240.0/255.0,28/255.0,1/255.0), width=1)
    plt.ylabel('Number of videos per gesture')
    plt.xticks(np.array(range(len(labels)), dtype=float) + 0.5, labels, rotation='vertical', size='small')
    # plt.xlim([-0.5, 249.5])
    plt.title('Chalearn LAP IsoGD Training Set')
    plt.savefig('/data4/szhou/figures/isogd_video_num_per_class.png')
    plt.show()


def main():
    labels, label_count = get_isogd_stats()
    draw_dataset_stats(labels, label_count)

if __name__ == '__main__':
    main()
