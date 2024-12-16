import os
import argparse
import sys
import shlex  # 用于正确地转义参数字符串
from typing import List


def get_command_line_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-method', type=str, default='CEC')
    parser.add_argument('-dataset', type=str, default='cifar')

    return parser


if __name__ == '__main__':
    # sys.argv[0] 是脚本名称，所以从 sys.argv[1:] 开始是传递给脚本的参数列表
    args_list = sys.argv[1:]
    
    # 创建一个新的列表来存储不包含'method'参数的参数
    filtered_args = []

    # 遍历原始参数列表
    skip_next = False  # 用于跳过'method'参数的值
    for i in range(len(args_list)):
        if skip_next:
            skip_next = False  # 跳过'method'的值
            continue
        if args_list[i] == '-method':
            skip_next = True  # 标记为跳过下一个值
            continue
        filtered_args.append(args_list[i])

    # 将过滤后的参数列表转换为一个单独的字符串，参数之间用空格分隔
    args_str = ' '.join(filtered_args)
    
    # 打印出参数字符串
    print(args_str)
    parser = get_command_line_parser()
    args, unknown = parser.parse_known_args()
    if args.method != 'S3C':
        if args.method == 'CEC':
            model_name = "CEC-CVPR2021/train.py"
        elif args.method == 'FACT':
            model_name = "CVPR22-Fact/train.py"
        elif args.method == 'CLOM':
            model_name = "CLOM/train.py"
        loc = model_name + ' ' + args_str
        # print(loc)
        os.system(f"python {loc}")
    else:
        if args.dataset == 'cifar':
            loc = 'bash ./S3C/run_cifar_s3c.sh'
            os.system(loc)
        elif args.dataset == 'cub200':
            loc = 'bash ./S3C/run_cub_s3c.sh'
            os.system(loc)
        elif args.dataset == 'mini_imagenet':
            loc = 'bash ./S3C/run_imagenet_s3c.sh'
            os.system(loc)
        else:
            print("Unknown dataset.")