import csv

class CsvReader:
    def __init__(self, filename):
        self.filename = filename
        self.file_data = []

    def read_file(self):
        self.open_file()
        reader = csv.reader(self.file, delimiter = ';')
        next(reader)
        for line in reader:
            line_data = {
                'nro_region': int(line[0]),
                'region': line[1],
                'provincia': line[2],
                'circunscripcion_senatorial': int(line[3]),
                'distrito': int(line[4]),
                'comuna': line[5],
                'circunscripcion_electoral': line[6],
                'local': line[7],
                'nro_mesa': int(line[8]),
                'tipo_mesa': line[9],
                'mesas_fusionadas': line[10],
                'electores': int(line[11]),
                'nro_en_voto': int(line[12]),
                'candidato': line[13],
                'votos_tricel': int(line[14])
            }
            self.file_data.append(line_data)
        self.close_file()
        return self.file_data
        
    def open_file(self):
        self.file = open(self.filename)

    def close_file(self):
        self.file.close()
