import Dictify, Dict_lst, sys
from Column import Column
#compare two csvs based on keys (columns arg)

#initially this will take column names (meaning that column names will have to be identical for each)
#but eventually it will do column numbers

#general goal: go through and compare the columns for each row to see if those values exist for those columsn in the other sheet 

class Csv_compare:
	def __init__(self, fname, columns= [], cust_name = ''):
		if not isinstance(columns, list): raise TypeError("columns parameter must be list")

		self.columns = columns
		self.data = Dict_lst.Dict_lst(Dictify.Dictify(fname).main())
		self.fname= fname
		self.data.add_crit('Match?', 'N!')
		self.data.add_crit('Reason', '')
		self.data.add_crit('C Reason', '')
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
	def compare_cols(self, target, columns):
		if not isinstance(target, Csv_compare): raise TypeError("Target must be Csv_compare object")
		row = []
		for i in range(0, len(self.data)):
			row = self.data.get_index(i)
			for j in range(0, len(target)):
				#compares row columns
				t_row = target.get_index(j)
				if self._compare_rows(row, t_row) and self._compare_rows_cols(row, t_row, columns): 
					row['Match?'] = 'Y'

					break
				else: row['Match?'] = 'N'
	def compare_keys(self, target,key, value_index):
		if not isinstance(target, Csv_compare): raise TypeError("Target must be Csv_compare object")
		value_col_name = self.columns[value_index][0]
		row = []
		for i in range(0, len(self.data)):
			row = self.data.get_index(i)
			for j in range(0, len(target)):
				#compares row columns
				t_row = target.get_index(j)
				if self._compare_row_keys(key,row, t_row):
					row['Match?'] = 'Index Match'
					row['Reason'] = t_row[value_col_name]

					break
				else: row['Match?'] = t_row[value_col_name]

	def match_up_rows_by_key(self,  target,key, value_index):
		
		for i in range(0, len(target.data.header)): self.data.add_crit("Matched_" + list(target.data.header)[i], '')

		if not isinstance(target, Csv_compare): raise TypeError("Target must be Csv_compare object")
		value_col_name = self.columns[value_index][0]
		row = []
		for i in range(0, len(self.data)):
			row = self.data.get_index(i)
			for j in range(0, len(target)):
				#compares row columns
				t_row = target.get_index(j)
				if self._compare_row_keys(key,row, t_row):
					row['Match?'] = 'Index Match'
					row['Reason'] = t_row[value_col_name]

					break
				else: row['Match?'] = t_row[value_col_name]
			if row['Match?']== 'Index Match':
				#for i in range(0, len(self.columns)): row["Matched_"+ self.columns[i][0]]= t_row[self.columns[i][0]]
				for i in range(0, len(target.data.header)):row['Matched_'+ list(target.data.header)[i]] = t_row[list(target.data.header)[i]]

	def export(self, cust_name = ''):
		if cust_name:
			self.data.export([], cust_name)
		else:
			self.data.export([], 'C_Results_'+self.fname)




	def _compare_rows(self, row, targ_row):
		#returns True if every self.columns column in row is equal to that in targ_row 
		for col in self.columns:
			if Column(col[0],col[1] ,row[col[0]]) != Column(col[0],col[1] ,targ_row[col[0]]):
				#print(str(row[col]), " DOes not match" , str(targ_row[col]))


				return False
		return True
	def _compare_rows_cols(self, row, targ_row, col_index):
		for ind in col_index:
			col = self.columns[ind]
			if Column(col[0],col[1] ,row[col[0]]) != Column(col[0],col[1] ,targ_row[col[0]]):
				row['C Reason'] = 'asdfasd' + targ_row[col[0]]
				return False
		return True
	def _compare_row_keys(self, key,  row, targ_row):
		#key is list of indexes (sans the index that you are attempting compare)
		for ind in key:
			col = self.columns[ind]
			if Column(col[0],col[1] ,row[col[0]]) != Column(col[0],col[1] ,targ_row[col[0]]):
				return False
		return True

print(__name__)


if __name__ == '__main__':
	print(sys.argv[1], type(sys.argv[1]))
	#need a parser
	#try:
		#[for args in sys.argv[1:]]

	#pass
'''
else:
	#fname = 'sql no rounding.csv'
	#t_fname = 'dfi export test.csv'
	fname  ='nupload 2021-11-01 to 11-30.csv'
	t_fname	 = 'dfi cmi 20211101 - 1130.csv'

	#columns = ['Department Code', 'Fleet Code']
	#columns = [('INV #',0), ('Customer #',0),('Date',0),('Item Code',0),('QTY',2),	('WHS',0), ('Unit Price', 2), ('Ext',2)]
	columns = [('INV #',0), ('Customer #',0),('Date',0),('Item Code',0),	('WHS',0), ('Unit Price', 2), ('Ext',2)]

	m_inst = Csv_compare(fname,columns)
	t_inst = Csv_compare(t_fname)
	#m_inst.compare_full(t_inst)
	#m_inst.compare_cols(t_inst, [7])
	#m_inst.compare_keys(t_inst,[0, 1, 2, 3, 4, 5,6],7)
	m_inst.compare_keys(t_inst,[0, 1, 2, 3, 4, 5],6)



'''