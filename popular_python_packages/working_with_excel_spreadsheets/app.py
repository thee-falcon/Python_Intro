import openpyxl

wb = openpyxl.load_workbook("transactions.xlsx")
print(wb.sheetnames)
sheet = wb["Sheet1"]

cell = sheet["a1"]
#cell = sheet.cell(row=1, column=1) # is the same code
#print(sheet.max_column) # will return a number 3
#print(sheet.max_row) # will return a number 4
# so lets print all values in the sheet
# for row in range(1, sheet.max_row + 1):
#     for col in range(1, sheet.max_column + 1):
#         cell = sheet.cell(row, col)
#         print(cell.value)

