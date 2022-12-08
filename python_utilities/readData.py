import pandas as pd
from xlrd import open_workbook

class readData:

    global sheet

    def import_excel(self, test_data):
        excelread = pd.read_excel(test_data, engine='openpyxl')
        # print(excelread)
        return excelread



    def full_excel_data(self,test_data):
        dict_list = []
        book = open_workbook(test_data)
        sheet = book.sheet_by_index(0)

        # read first row for keys
        keys = sheet.row_values(0)

        # read the rest rows for values
        values = [sheet.row_values(i) for i in range(1, sheet.nrows)]

        for value in values:
            dict_list.append(dict(zip(keys, value)))

        return dict_list

    def getData(self, test_data, row_num):
        # full_data = self.full_excel_data(test_data)
        full_data1 = self.import_excel(test_data)
        return full_data1.loc[row_num].to_dict()

        # print(dict_list)

# readdata_obj = readData()
# data = readdata_obj.getData("..\\test_data\\Book3.xlsx", 1)
# print(data)



