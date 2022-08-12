class TablesByRegionExporter:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def export(self):
        self.count_tables_by_region()
        self.write_to_file()


    def count_tables_by_region(self):
        self.tables_by_region = {}
        for table in self.data:
            if table['region'] in self.tables_by_region:
                self.tables_by_region[table['region']] += 1
            else:
                self.tables_by_region[table['region']] = 1

    def get_unique_regions(self):
        return list(self.tables_by_region.keys())

    def write_to_file(self):
        file = open(self.filename, 'w')
        for region in self.get_unique_regions():
            file.write(f'{region};{self.tables_by_region[region]}\n')
        file.close()