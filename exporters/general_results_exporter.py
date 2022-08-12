class GeneralResultsExporter:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def export(self):
        self.count_results()
        self.write_to_file()

    def count_results(self):
        self.count = {}
        for table in self.data:
            if table['candidato'] not in self.count:
                self.count[table['candidato']] = 1
            else:
                self.count[table['candidato']] += table['votos_tricel']

    def get_unique_candidates(self):
        return list(self.count.keys())

    def write_to_file(self):
        file = open(self.filename, 'w')
        for candidate in self.get_unique_candidates():
            file.write(f'{candidate};{self.count[candidate]}\n')
        file.close()