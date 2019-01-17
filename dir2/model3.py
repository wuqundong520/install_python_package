import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./../"))
from dir1.model2 import fun2


def fun3():
    print(" fun3 to invoke fun2")
    fun2()

if __name__ == '__main__':
    fun3()
