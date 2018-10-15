import json 
import os.path
from flask import Flask
app = Flask( __name__ )


@app.route( '/' )
def landingPage():
	return "To query data, add /forex/ to the url followed by the currency pair.\nExample: /forex/USDJPY" 

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



