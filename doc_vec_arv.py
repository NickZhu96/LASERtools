#input是embed.sh之后生成的二进制文件
#python doc_vec_arv.py -i INPUT -o OUTPUT
#提取input文件后，对N行1024维数列进行arv pooling，输出为1行1024维度的vector

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
c = X.shape[0]
b = np.sum(X,axis=0)
b = b / c
b.resize(b.shape[0] // dim , dim)
np.savetxt("{}".format(args.output),b)
