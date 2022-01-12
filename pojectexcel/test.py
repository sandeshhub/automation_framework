import  gspread
sa = gspread.service_account("creds.json")

sh = sa.open('alpasal_auto_test')

wks =sh.worksheet('store')

#print('Rows',wks.row_count)
#print('Column',wks.col_count)

#print(wks.acell('B5').value)
#print(wks.cell(3,4).value)

#print(wks.get('A1:F5'))

print(wks.get_all_records())






