# 作者：乾
# 时间：2025年02月19日
# Mail:chb8572@gamil.com
import copy


def copy_shallow_test():  # 浅拷贝 仅拷贝第一层,对于嵌套内部的对象，拷贝的是对象的引用
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = a.copy()
    c = a.copy()  # 浅拷贝
    b[0] = [11, 22, 33]
    c[0][0] = 3
    print(a)
    print(b)
    print(c)


def copy_deep_test():  # 深拷贝 递归拷贝所有层级的对象
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    b[0] = [11, 22, 33]
    c[0][0] = 3
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    copy_shallow_test()
    print("-"*50)
    copy_deep_test()
