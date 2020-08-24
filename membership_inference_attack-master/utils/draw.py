
import numpy as np
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt 
def main():
    # path = '/opt/kxp/workspace/dp-project/membership_inference_attack-master/results/MNIST_overfitting_2020_08_24_23_47_21/res_accuracy_per_class.npy'
    # res_accuracy_per_class = np.load(path)
    # print(res_accuracy_per_class)
    # x= np.linspace(1, 10, 10)
    # plt.plot(x, res_accuracy_per_class[0], 'ro-')
    # plt.title('The acc per class')
    # plt.xlabel('class')
    # plt.ylabel('accuracy')
    # plt.legend()
    # # plt.show()
    # plt.savefig('mnist-acc-class.png', dpi=300)

    # path = '/opt/kxp/workspace/dp-project/membership_inference_attack-master/results/MNIST_overfitting_2020_08_24_23_47_21/res_recall_per_class.npy'
    # res_accuracy_per_class = np.load(path)
    # print(res_accuracy_per_class)
    # x= np.linspace(1, 10, 10)
    # plt.plot(x, res_accuracy_per_class[0], 'go-')
    # plt.title('The recall per class')
    # plt.xlabel('class')
    # plt.ylabel('recall')
    # plt.legend()
    # # plt.show()
    # plt.savefig('mnist-recall-class.png', dpi=300)

    path = '/opt/kxp/workspace/dp-project/membership_inference_attack-master/results/MNIST_overfitting_2020_08_24_23_47_21/res_precision_per_class.npy'
    res_accuracy_per_class = np.load(path)
    # print(res_accuracy_per_class)
    x= np.linspace(1, 10, 10)
    plt.plot(x, res_accuracy_per_class[0], 'bo-')
    plt.title('The precision per class')
    plt.xlabel('class')
    plt.ylabel('precision')
    plt.legend()
    # plt.show()
    plt.savefig('mnist-precision-class.png', dpi=300)


if __name__ == '__main__':
    main()