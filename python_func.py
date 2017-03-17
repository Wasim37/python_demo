# _*_ coding: utf-8 _*_

from operator import add
from functools import partial, reduce

# 列表解析
# a_list = [item**2 for item in range(5)]
# print(a_list)
# print(a_list[2])

# # enumerate函数
# for index, item in enumerate(range(5)):
#     print("%d: %d" % (index, item))

# 字典解析
# a_dict = {item: item**2 for item in range(5)}
# print(a_dict)
# b_dict = {"%d^2" % item: item**2 for item in range(5)}
# print(b_dict)

# 生成器
# a_generator = (item**2 for item in range(5))
# print(a_generator)
# print(next(a_generator))
# print(next(a_generator))
# print(next(a_generator))
# print(next(a_generator))
# print(next(a_generator))

# iter函数和next函数
# a_list_generator = iter(a_list)
# print(next(a_list_generator))
# print(next(a_list_generator))
# print(type(a_list), type(a_list_generator))

# # lambda表达式
# a_func = lambda x, y: x**y
# print(a_func(2, 3))

# map函数
# abs()函数是返回绝对值
# print(map(abs, range(-4, 5)))
# print(list(map(abs, range(-4, 5))))
# print(list(map(lambda x: x**2, range(5))))
# print(list(map(lambda x, y: x**y, range(1, 5), range(1, 5))))

# # reduce函数
# # 用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果
# # reduce()还可以接收第3个可选参数，作为计算的初始值
# print(reduce(lambda x, y: x+y, range(10)))
# print(reduce(lambda x, y: x+y, range(5), 100))
print(reduce(lambda x, y: x+y, [[1], [3, 4]]))
print(reduce(lambda x, y: x+y, [[1, 2], [3, 4]]))
print(reduce(lambda x, y: x+y, [[1, 2], [3, 4], [3]]))
print(type(([1, 2], [3, 4], [3]))) # tuple为元组
print(type([[1, 2], [3, 4], [3]]))

#
# # filter函数
# print(filter(None, range(-4, 5)))
# print(list(filter(None, range(-4, 5))))
# print(list(filter(lambda x: x > 0, range(-4, 5))))

# any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
# all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
# print(all([0, 1, 2]))
# print(any([0, 1, 2]))

# zip函数
# zip([seql, ...])接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
# 若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
# xy = zip([1, 2, 3], ["a", "b", "c"])
# print xy
# for a, b in xy:
#     print(a, b)
# a_dict = dict(zip([1, 2, 3], ["a", "b", "c"]))
# print(a_dict)
# a_dict = dict([(21, 'asda'), (2, 'b'), (3, 'c')])
# print(a_dict)

# int函数
# (1)10010要以字符串的形式进行输入，如果是带参数base的话
# (2)这里并不是将10010转换为16进制的数，而是说12就是一个16进制的数，int()函数将其用十进制数表示
# print(int("10010", base=2))

# partial函数
# 一个函数可以有多个参数，而在有的情况下有的参数先得到，有的参数需要在后面的情景中才能知道，python 给我们提供了partial函数用于携带部分参数生成一个新函数
# int_base_2 = partial(int, base=2)
# print(int_base_2("10010"))

# # operator.add函数
# print(reduce(lambda x, y: x+y, range(10)))
# print(reduce(add, range(10)))


