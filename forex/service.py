import json 
import os.path
from flask import Flask
app = Flask( __name__ )

PAIRS = [ x.split('.')[0] for x in os.listdir('jsonData') if x.endswith( 'json' ) ]

@app.route( '/' )
def landingPage():
    message = "<html><body><p>To query data, add /forex/ to the url followed by the currency pair.<br>\nExample: /forex/USDJPY<br><br>Available pairs:<br>"
    for p in PAIRS:
        message += "%s<br>\n" % p
    message += "</body></html>"
    return message

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
    app.run( host='0.0.0.0', port=8081 )



