# -*- coding: utf-8 -*-
"""
@author:puzhen
@data:2023/5/15 21:46
"""

# 将图片和标注数据按比例切分为 训练集和测试集
import shutil
import random
import os

# 原始路径
image_original_path = "E:/实验数据/土豆CT实验/images/"
label_original_path = "E:/实验数据/土豆CT实验/labels/"
image_last_name = '.png'
label_last_name = '.txt'

cur_path = os.getcwd()

# 训练集路径
train_image_path = os.path.join(cur_path, "datasets/defect/images/train/")
train_label_path = os.path.join(cur_path, "datasets/defect/labels/train/")

# 验证集路径
val_image_path = os.path.join(cur_path, "datasets/defect/images/val/")
val_label_path = os.path.join(cur_path, "datasets/defect/labels/val/")

# 测试集路径
test_image_path = os.path.join(cur_path, "datasets/defect/images/test/")
test_label_path = os.path.join(cur_path, "datasets/defect/labels/test/")

# 训练集目录
list_train = os.path.join(cur_path, "datasets/defect/train.txt")
list_val = os.path.join(cur_path, "datasets/defect/val.txt")
list_test = os.path.join(cur_path, "datasets/defect/test.txt")

train_percent = 0.4
val_percent = 0.4
test_percent = 0.4


def del_file(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        os.remove(file_data)


def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    else:
        del_file(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)
    else:
        del_file(train_label_path)

    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    else:
        del_file(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)
    else:
        del_file(val_label_path)

    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    else:
        del_file(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)
    else:
        del_file(test_label_path)


def clearfile():
    if os.path.exists(list_train):
        os.remove(list_train)
    if os.path.exists(list_val):
        os.remove(list_val)
    if os.path.exists(list_test):
        os.remove(list_test)


def main():
    mkdir()
    clearfile()

    file_train = open(list_train, 'w')
    file_val = open(list_val, 'w')
    file_test = open(list_test, 'w')

    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)
    list_all_txt = range(num_txt)

    num_train = int(num_txt * train_percent)
    num_val = int(num_txt * val_percent)
    num_test = num_txt - num_train - num_val

    train = random.sample(list_all_txt, num_train)
    # train从list_all_txt取出num_train个元素
    # 所以list_all_txt列表只剩下了这些元素
    val_test = [i for i in list_all_txt if not i in train]
    # 再从val_test取出num_val个元素，val_test剩下的元素就是test
    val = random.sample(val_test, num_val)

    print("训练集数目：{}, 验证集数目：{}, 测试集数目：{}".format(len(train), len(val), len(val_test) - len(val)))
    for i in list_all_txt:
        name = total_txt[i][:-4]

        srcImage = image_original_path + name + image_last_name
        srcLabel = label_original_path + name + ".txt"

        if i in train:
            dst_train_Image = train_image_path + name + image_last_name
            dst_train_Label = train_label_path + name + label_last_name
            shutil.copyfile(srcImage, dst_train_Image)
            shutil.copyfile(srcLabel, dst_train_Label)
            file_train.write(dst_train_Image + '\n')
        elif i in val:
            dst_val_Image = val_image_path + name + image_last_name
            dst_val_Label = val_label_path + name + label_last_name
            shutil.copyfile(srcImage, dst_val_Image)
            shutil.copyfile(srcLabel, dst_val_Label)
            file_val.write(dst_val_Image + '\n')
        else:
            dst_test_Image = test_image_path + name + image_last_name
            dst_test_Label = test_label_path + name + label_last_name
            shutil.copyfile(srcImage, dst_test_Image)
            shutil.copyfile(srcLabel, dst_test_Label)
            file_test.write(dst_test_Image + '\n')

    file_train.close()
    file_val.close()
    file_test.close()


if __name__ == "__main__":
    main()