'''
绝对导入:需要指明这个模块，函数的完整路径，或希望导入的路径
相对导入: 找出一个类，函数或者模块，它的定位相对与当前模块， ps:想想相对路径
'''

# 绝对导入 导入helloworld模块
# import day01.helloworld
# resutl = day01.helloworld.first_py_program()
# 或者
# from day01.helloworld import first_py_program
# result = first_py_program()
# print(result)

'''相对导入 helloworld模块的Hello类, 用一个点代表当前包， 更多点代表更上层
 ps:在涉及相对导入时，package所在文件夹必须被Python解释器视为package,不是普通文件夹
 被视为package的条件：
 1,文件夹中必须有__init__.py(可为空)文件
 2,不能作为顶层模块来执行该文件夹的.py文件(即不能作为主函数的入口)
 
 ps: 程序执行时__name__的值是__main__, 而模块被导入时'.'代表了模块所在的package名称，程序执行时'.'
 就变成了__main__, 所以抛出__main__ is not a package, 此时需使用绝对导入， 相对导入时程序入口必须不
 在当前文件内
'''
# 错误的演示 由于在该py执行，此时该文件时程序入口 下面导入将失败
# from .helloworld import first_py_program
# hello = firsst_py_program()
# print(hello)

# 正确姿势, 在该文件下相对导入helloworld 模块的函数，在main.py执行
from .helloworld import first_py_program
