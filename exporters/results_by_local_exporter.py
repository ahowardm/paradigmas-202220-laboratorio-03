class ResultsByLocalExporter:
    def __init__(self, data, local):
        self.data = data
        self.local = local

    def export(self):
        self.filter_tables()
        self.count_results()
        return self.count

    def filter_tables(self):
        self.tables_in_local = [x for x in self.data if x['local'] == self.local]

    def count_results(self):
        self.count = {}
        for table in self.tables_in_local:
            if table['candidato'] not in self.count:
                self.count[table['candidato']] = 1
            else:
                self.count[table['candidato']] += table['votos_tricel']

    def get_unique_candidates(self):
        return list(self.count.keys())
