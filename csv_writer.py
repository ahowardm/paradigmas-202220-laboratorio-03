class CsvWriter:
	def __init__(self, filename, data):
		self.filename = filename
		self.data = data

	def get_unique_keys(self):
		return list(self.data.keys())

	def write_to_file(self):
		file = open(self.filename, 'w')
		for key in self.get_unique_keys():
			file.write(f'{key};{self.data[key]}\n')
		file.close()