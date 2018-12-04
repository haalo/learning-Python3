'''
第一个Python3程序
'''


def first_py_program():
    string = 'Hello World!'
    return string


class Hello:

    def __init__(self, string='hello world'):
        self.string = string

    def say(self):
        print(self.string)

print(__name__)
