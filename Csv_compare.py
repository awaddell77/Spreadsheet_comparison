import Dictify, Dict_lst, sys

#compare two csvs based on keys (columns arg)

#initially this will take column names (meaning that column names will have to be identical for each)
#but eventually it will do column numbers

#general goal: go through and compare the columns for each row to see if those values exist for those columsn in the other sheet 

class Csv_compare:
	def __init__(self, fname, columns= [], cust_name = ''):
		if not isinstance(columns, list): raise TypeError("columns parameter must be list")
		self.columns = columns
		self.data = Dict_lst.Dict_lst(Dictify.Dictify(fname).main())
		self.data.add_crit('Match?', 'N!')
		self.cust_name = str(cust_name)
	def __len__(self):
		return len(self.data)
	def get_index(self, loc):
		return self.data.get_index(loc)
	def compare_full(self, target):
		#will compare every single row in data to every single row in target 
		#once it finds a match in target it places a Y in the Match column and stops comparing 

		if not isinstance(target, Csv_compare): raise TypeError("Target must be Csv_compare object")
		row = []
		for i in range(0, len(self.data)):
			row = self.data.get_index(i)
			for j in range(0, len(target)):
				#compares row columns
				t_row = target.get_index(j)
				if self._compare_rows(row, t_row): 
					row['Match?'] = 'Y'
					break
				else: row['Match?'] = 'N'
	def export(self, cust_name = ''):
		if cust_name:
			self.data.export([], cust_name)
		else:
			self.data.export([], 'C_Results_'+fname)




	def _compare_rows(self, row, targ_row):
		#returns True if every self.columns column in row is equal to that in targ_row 
		for col in self.columns:
			if row[col] != targ_row[col]:
				return False
		return True



fname = 'tab1fromsheet.csv'
t_fname = 'petroleaderaccountscards.csv'
columns = ['Department Code', 'Fleet Code']
m_inst = Csv_compare(fname,columns)
t_inst = Csv_compare(t_fname)
m_inst.compare_full(t_inst)



if __name__ == 'main':
	pass

