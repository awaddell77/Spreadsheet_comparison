


class Column:
	_t_map = (str, int, float)
	def __init__(self, name, data_type, value):
		self.name = name
		self.data_type = self._t_map[data_type]
		self.value = value

	def __eq__(self, t_column):
		if not isinstance(t_column, Column): raise TypeError("Must be Column")
		if t_column.data_type is self.data_type: return self.data_type(self.value) == self.data_type(t_column.value)
		else: return str(self.value) == str(t_column.value)



