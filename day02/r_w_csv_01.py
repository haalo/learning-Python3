'读写csv数据，使用csv库操作csv_files目录下的stocks.csv文件'
import csv
from collections import namedtuple


def r_csv_01(filename):
    '''
    将csv文件数据读取为一个元组序列
    :param filename: csv文件名
    :return:
    '''
    with open(filename) as f: # 创建文件对象，with在操作完成后自动关闭文件
        # delimiter = ',' 以，作为行分割符
        f_csv = csv.reader(f, delimiter=',') # 传入文件对象构建csv的reader对象，读取操作基于该reader
        headers = next(f_csv) # 读取第一行，next(csv.reader)读取一行，并且文件指针永远加1，即指向下一行
        for row in f_csv:
            # 由于前面调用了next()，此时从文件第二行开始读取，row是一个元组序列
            # 可通过下标访问字段
            # 访问Symbol
            print('Symbol', row[0])
            # 访问Change
            print('Change', row[4])
            # 输出整行
            print(row)
            print('-' * 50)


def r_csv_02(filename):
    '''
    由于下标会引起混淆，可以使用命名元组,需导入库collections.namedtuple
    :param filename: csv文件名
    :return:
    '''
    with open(filename) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row  = namedtuple('Row', headings)  # 命名元组
        for r in f_csv:
            row = Row(*r) # 命名元组
            # 输出
            print('Symbol', row.Symbol)
            print('Change', row.Change)
            print(row)
            print('=' * 50)


def r_csv_03(filename):
    '''
    将csv数据读取到一个字典中
    :param filename:
    :return:
    '''
    with open(filename) as f:
        f_csv = csv.DictReader(f) # DictReader
        for row in f_csv:
            # 可使用列名访问数据
            print('Symbol', row['Symbol'])
            print('Change', row['Change'])
            print(row)
            print('$' * 50)


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [("BB", 11.11, "11/11/2011", "11:11am", -1.11, 111111)] * 3

def w_csv_01(filename):
    '''
    写入headers和rows数据到csv文件中，使用csv模块
    :param filename:
    :return:
    '''
    with open(filename, 'w') as f:
        # 1， 创建writer对象
        f_csv = csv.writer(f)
        # 写入列名
        f_csv.writerow(headers)
        # 写入数据行
        f_csv.writerows(rows)

    print('----------done-------------')


def w_csv_02(filename):
    '''
    写入字典序列的数据
    :param filename:
    :return:
    '''
    rows = [{'Symbol': 'AA', 'Price': 39.88, 'Date': '11/11/2001',
             'Time': '11:11', 'Change': -0.18, 'Volume': 1111111}] * 4

    with open(filename, 'w') as f:
        f_csv = csv.DictWriter(f, headers) # 传入文件对象和字段元组
        f_csv.writeheader() # 写入头行（列名）
        f_csv.writerows(rows)
    print('----------done-------------')


def main():
    # filename = 'csv_files/stocks.csv'

    # 读取
    # r_csv_01(filename) #普通读取
    # r_csv_02(filename) #命名元组
    # r_csv_03(filename) # 读取到字典

    # 写入
    filename = 'csv_files/stocks01.csv'
    # w_csv_01(filename)
    w_csv_02(filename)
if __name__ == '__main__':
    main()
