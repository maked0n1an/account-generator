import csv  
import xlsxwriter

from pathlib import Path 

from modules.writer import Writer


class CsvWriter(Writer):
    def __init__(self, filename: str):
        self.create_folder()
        self.full_path = Path(Writer.folder_name) / (filename + '.csv')
    
    def write_data(self, data):
        with open(self.full_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)            
            csv_writer.writerow(Writer.header)
            
            csv_writer.writerows(data)


class ExcelWriter(Writer):
    def __init__(self, filename: str):
        self.create_folder()
        self.full_path = Path(Writer.folder_name) / (filename + '.xlsx') 
    
    def write_data(self, data):        
        workbook = xlsxwriter.Workbook(self.full_path)
        worksheet = workbook.add_worksheet()
        
        bold_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
        
        worksheet.write_row(0, 0, Writer.header, bold_format)
        
        for row, account_data in enumerate(data, start=1):
            worksheet.write_row(row, 0, account_data)
        
        workbook.close()