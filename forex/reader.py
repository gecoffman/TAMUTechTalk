

import pandas
import json
DIR_NAME = 'data' 
FILE_NAMES = [ 'AUDUSD.csv', 'EURUSD.csv', 'GBPUSD.csv', 'NZDUSD.csv', 
'USDCAD.csv', 'USDCHF.csv', 'USDJPY.csv' ] 

def getData():
	data = {} 
	for fileName in FILE_NAMES:
		df = pandas.read_csv( DIR_NAME + '/' + fileName )
		df.columns = [ 'DateTime', 'Close', 'High', 'Low', 'Open' ] 
	
		data[ fileName ] =  df
	return data 

def formatData( data ):
	for name, df in data.iteritems():
		j = df.to_json(orient='records')
		with open( 'jsonData/' + name[:-4] + '.json', 'w') as outfile:
    			json.dump(j, outfile)		 

def main():
	data = getData()
	formatData( data )
if __name__ == '__main__':
	main()
