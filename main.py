from parse_options import ParseOptions
from csv_reader import CsvReader
from csv_writer import CsvWriter

from exporters.tables_by_region_exporter import TablesByRegionExporter
from exporters.general_results_exporter import GeneralResultsExporter
from exporters.results_by_local_exporter import ResultsByLocalExporter

def ask_for_filename():
    return input('Ingresa el nombre del archivo de salida: ')

if __name__ == '__main__':
    data = []
    while True:
        option_selected = ParseOptions.get_option()
        if option_selected == 0:
            exit(0)
        elif option_selected == 1:
            filename = input('Ingresa el nombre del archivo de datos: ')
            reader = CsvReader(filename)
            data = reader.read_file()
        elif option_selected == 2:
            filename = ask_for_filename()
            exporter = TablesByRegionExporter(data)
            exported_data = exporter.export()
            writer = CsvWriter(filename, exported_data)
            writer.write_to_file()
        elif option_selected == 3:
            filename = ask_for_filename()
            exporter = GeneralResultsExporter(data)
            exported_data = exporter.export()
            writer = CsvWriter(filename, exported_data)
            writer.write_to_file()
        elif option_selected == 4:
            filename = ask_for_filename()
            local = input('Ingresa el nombre del local a graficar (debe estar igual que en el archivo): ')
            exporter = ResultsByLocalExporter(data, local)
            exported_data = exporter.export()
            writer = CsvWriter(filename, exported_data)
            writer.write_to_file()
