class TablesByRegionExporter:
    def __init__(self, data):
        self.data = data

    def export(self):
        self.count_tables_by_region()
        return self.tables_by_region

    def count_tables_by_region(self):
        self.tables_by_region = {}
        for table in self.data:
            if table['region'] in self.tables_by_region:
                self.tables_by_region[table['region']] += 1
            else:
                self.tables_by_region[table['region']] = 1

    def get_unique_regions(self):
        return list(self.tables_by_region.keys())
