# Wal IN dIR
import os

for root, dir, files in os.walk("/Users/promode/PycharmProjects/Py3xATBLearning/ex02_July/05072024"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"files Dir Dir {files}")
    print(len(files))