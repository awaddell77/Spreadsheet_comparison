
from Csv_compare import *
#fname = 'sql no rounding.csv'
#t_fname = 'dfi export test.csv'
fname  ='nupload 2021-11-01 to 11-30.csv'
t_fname	 = 'dfi cmi 20211101 - 1130.csv'

#columns = ['Department Code', 'Fleet Code']
#columns = [('INV #',0), ('Customer #',0),('Date',0),('Item Code',0),('QTY',2),	('WHS',0), ('Unit Price', 2), ('Ext',2)]
columns = [('INV #',0), ('Customer #',0),('Date',0),('Item Code',0),	('WHS',0), ('Unit Price', 2), ('Ext',2)]

m_inst = Csv_compare(fname,columns)
t_inst = Csv_compare(t_fname)

#m_inst.compare_keys(t_inst,[0, 1, 2, 3, 4, 5,6],7) #compares everything inv#, customer#, date, itemcode, qTY, whs, unit price, and returns ext
#m_inst.compare_keys(t_inst,[0, 1, 2, 3, 4, 5],6)#compares  inv#, customer#, date, itemcode, whs, unit price, and returns ext [no QTY comparison]
m_inst.match_up_rows_by_key(t_inst,[0, 1, 2, 3, 4, 5],6)
m_inst.export()
