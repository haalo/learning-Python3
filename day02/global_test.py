'''global关键字
内部作用域想要对外部作用域的变量进行修改
'''
NUM = 1

def fun():
    NUM = 3
    print('函数内部:', NUM)


def fun_use_global():
    global NUM
    NUM = 3
    print('函数内部: ', NUM )


if __name__ == '__main__':
    fun()
    print('没有使用global: ', NUM)

    fun_use_global()
    print('使用global: ', NUM)
