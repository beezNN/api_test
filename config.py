#coding=utf-8

import xlrd



class Read_xlsx(object):
    def __init__(self, filepath):
        self.file = xlrd.open_workbook(filepath)
        self.sh = self.file.sheet_by_index(0)

    def info(self):
        data = []
        for romnum in range(1, self.sh.nrows):
            # print(self.sh.row_values(romnum))
            data.append(self.sh.row_values(romnum))
        return data
state = '登录'

# a = Read_xlsx("case.xlsx").info()
# print(a)