'''
Created on Oct 11, 2018

@author: Tanner Yilmaz
'''
import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

# Applying multiple styles 
style = xlwt.easyxf('font: bold 1, color red;')

for i in range(1,101): #nested loops traverse the excel file cells
    for k in range(1,101):
        sheet1.write(i , k, f'Cell:{i,k}', style) 
   
wb.save('Sheet_1.xls') #saving file 
print("Sheet saved")