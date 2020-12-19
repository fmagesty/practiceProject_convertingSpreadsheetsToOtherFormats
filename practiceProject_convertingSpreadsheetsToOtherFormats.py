# Script that uses Google Sheets to convert a spreadsheet file into other formats.
# Upload the spreadsheet and it is downloaded as an Excel file and converts it to other formats aswell.

import ezsheets

# Uploads the spreadsheet.
print('Enter the name of spreadsheet:')
fileName = input() + '.xlsx'
ss = ezsheets.upload(str(fileName))

print('Downloading a copy of your .xlsx file.')
# Download it as Excel.
ss.downloadAsExcel('copy of' + str(fileName))
# Converts it to other formats as a copy.
print('Downloading as .ODS...')
ss.downloadAsODS()
print('Downloading as .CSV...')
ss.downloadAsCSV()
print('Downloading as .TSV...')
ss.downloadAsTSV()
print('Downloading as .PDF...')
ss.downloadAsPDF()
print('Downloading as HTML...')
ss.downloadAsHTML()
print('Done.')