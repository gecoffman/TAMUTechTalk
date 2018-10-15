import json 
import os.path
from flask import Flask
app = Flask( __name__ )


@app.route( '/' )
def returnSingle():
	return "hello world" 

@app.route( '/forex/<ccyPair>' )
def returnCCYData( ccyPair ):
	if os.path.isfile( 'jsonData/' +  ccyPair + '.json' ):
		with open( 'jsonData/' + ccyPair + '.json' ) as json_data:
			d = json.load( json_data )
			json_data.close()
			return d
	else:
		return 'Currency pair does not exist. Try again'   

if __name__ == "__main__":
    app.run()



