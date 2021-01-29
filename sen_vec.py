#input是embed.sh生成的二进制文件
#python sen_vec.py -i INPUT -o OUTPUT
#input文件包含几行文本就会输出几行1024维度向量


import numpy as np
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--input','-i',help='input a file')
parser.add_argument('--output','-o',help='output to a file')
args = parser.parse_args()

dim = 1024
X = np.fromfile("{}".format(args.input), dtype=np.float32, count=-1)
X.resize(X.shape[0] // dim, dim)

np.savetxt("{}".format(args.output),X)
