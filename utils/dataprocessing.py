# coding:utf-8


import os
import random


'''
    使用前得更改源路径和保存路径 确保正确即可
'''



def get_files(path, res_list):
    try:
        tmp_l = os.listdir(path)
        for i in tmp_l:
            path_tmp = os.path.join(path, i)
            get_files(path_tmp, res_list)
    except:
        res_list.append(path)
        
# 按比例分数据集 p1训练集比例 p2验证集比例 p3测试集比例
def split_dataset(res_list, p1, p2, p3):
    size = len(res_list)
    axis1 = int(size * p1)
    axis2 = int(size * (p1 + p2))
    axis3 = size
    train_l = res_list[:axis1]
    val_l = res_list[axis1:axis2]
    test_l = res_list[axis2:axis3]
    return train_l, val_l, test_l


def save_data(src_path, dest_path):
    command_str = 'copy' + ' ' + src_path + ' ' + dest_path
    print(command_str)
    try:
        os.system(command_str)
    except:
        exit('error!')    


if __name__ == "__main__":
    
    path = r'E:\NEW\Myfile\yoloproject\code\MEMS100_copy\labels'
    resList = []
    get_files(path, resList)
    train, val, test = split_dataset(resList, 0.8, 0.1, 0.1)
    destTrainPath = r"C:\Users\dell\Desktop\dataset\label\train"
    destValPath = r"C:\Users\dell\Desktop\dataset\label\val"
    destTestPath = r"C:\Users\dell\Desktop\dataset\label\test"
    for elem in train:
        save_data(elem, destTrainPath)
    for elem in val:
        save_data(elem, destValPath)
    for elem in test:
        save_data(elem, destTestPath)