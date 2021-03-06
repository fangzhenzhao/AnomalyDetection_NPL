ID_DS_LIST=("MNIST", "CIFAR10", "SVHN")
ID_MODEL_LIST=("LeNet", "VGG", "ResNet")
OOD_DS_LIST_MNIST         = ("FASHION_MNIST", "OMNIGLOT_RESIZED_28", "MNIST_GAUSSIAN_NOISE_ODIN", "MNIST_UNIFORM_NOISE")
OOD_DS_LIST_CIFAR10       = ("TINYIMAGENET_RESIZED_32","LSUN_RESIZED", "ISUN_PATCHED", "SVHN_CROPPED", "G_255", "U_255")

OOD_DS_LIST_SVHN       = ("TINYIMAGENET_RESIZED_32","LSUN_RESIZED", "ISUN_PATCHED", "CIFAR10",  "G_255", "U_255")
OOD_DS_LIST_CIFAR100      = OOD_DS_LIST_CIFAR10
PER_MAGNITUDE_LIST = [0.0, 0.0005, 0.001, 0.0015, 0.002, 0.0025, 0.005, 0.01, 0.05, 0.1, 0.15, 0.2]

OOD_APPROACHES = ("ours", "ours_w_p" , "softmax", "odin_wo_p", "odin_w_p", "mah_dist_logits", "mah_dist_logits_w_p") 
