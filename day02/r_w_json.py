'''
读写JSON数据
JSON编码支持的基本数据类型:None, bool, int, float和str,以及包含这些类型
的lists, tuples和dictionaries
可通过pprint()更好地打印数据
'''

import json
'''处理字符串用json.dumps()和json.loads()'''
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# 将python数据结构转换成JSON
json_str = json.dumps(data)
print(json_str)
# 将JSON编码的字符串转换回python数据结构
data = json.loads(json_str)
print(data)

'''处理文件用json.dump()和json.load()'''
def json_file(filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    # and
    with open(filename, 'r') as f:
        json.load(f)

'''JSON一般会解码提供的数据创建dicts和lists, 
    如果创建其他类型的对象,可以给json.loads()传递
    object_pairs_hook或object_hook参数'''
from collections import OrderedDict
def other_json():
    s = '{"name":"ACME", "shares":30, "price":49}'
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

other_json()

import sqlite3

