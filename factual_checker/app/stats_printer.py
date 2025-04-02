import csv
from datetime import datetime

class CsvPrinter:
    __file_header = ['Nume', 'Data', 'Credibilitate', 'Număr declarații', 'False', 'Trunchiate', 'Parțial adevărate', 'Adevărate']

    def __init__(self, file_path):
        self.file_path = file_path

    def print_politicians(self, stats):
        current_date = datetime.now().strftime('%Y-%m-%d')
        with open(self.file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(CsvPrinter.__file_header)
            for stat in stats:
                writer.writerow([
                    stat.name,
                    current_date,
                    stat.credibility,
                    stat.total,
                    stat.false_count,
                    stat.truncated_count,
                    stat.partially_true_count,
                    stat.true_count
                ])