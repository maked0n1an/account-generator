from modules.file_writers import ExcelWriter, CsvWriter
from utils import ValidationException


class WriterFactor:
    result_folder = 'results'
    
    @staticmethod
    def create_writer(format_type, filename):
        if format_type == 'Excel':
            return ExcelWriter(filename)
        elif format_type == 'CSV':
            return CsvWriter(filename)
        else:
            raise ValidationException(f'Unsupported format: {format_type}')