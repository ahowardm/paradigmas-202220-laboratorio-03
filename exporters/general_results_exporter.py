class GeneralResultsExporter:
    def __init__(self, data):
        self.data = data

    def export(self):
        self.count_results()
        return self.count

    def count_results(self):
        self.count = {}
        for table in self.data:
            if table['candidato'] not in self.count:
                self.count[table['candidato']] = 1
            else:
                self.count[table['candidato']] += table['votos_tricel']

    def get_unique_candidates(self):
        return list(self.count.keys())
