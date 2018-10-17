from flask import Flask, request
from datetime import datetime
import re
import os
import pandas as pd

app = Flask( __name__ )

def loadAllData():
    d = {}
    dataFiles = [ x for x in os.listdir('data') if x.endswith('.csv') ]
    for f in dataFiles:
        print 'reading file: %s' % f
        symbol = f.split('.')[0]
        df = pd.read_csv( 'data/' + f )
        df['Date'] = [ datetime.strptime( x, '%m/%d/%y' ) for x in df['Date'] ]
        df.index = df['Date']
        print df.head()
        d[ symbol ] = df
        print 'read %s' % f
    return d

def f_encode( df ):
    return df.to_csv()

def rangeAsFix( symbol, start, end ):
    if not start:
        return "FATAL: start is a mandatory parameter."
    if not end:
        return "FATAL: end is a mandatory parmmedery"
    if not re.match( r'^\d{6}$', start ):
        return "FATAL: start is not a date of the form YYMMDD."
    if not re.match( r'^\d{6}$', end ):
        return "FATAL: end is not a date of the form YYMMDD."
    try:
        s = datetime.strptime( start, '%y%m%d' )
        e = datetime.strptime( end,   '%y%m%d' )
    except:
        return "FATAL: cannot cast one of start, end as valid date"
    d = _DATA.get( symbol )

    if d is None:
        return "ERROR: cannot find data for SYMBOL %s" % symbol

    mask = (d['Date'] >= s) & (d['Date'] <= e)
    d = d.loc[mask]
    return f_encode( d )


@app.route( '/' )
def landingPage():
    message  = "To query data, add /equity/ to the url followed by a symbol,<br>\n"    
    message += "supplying mandatory parameters start and end each in the form YYMMDD.<br>\n\n"
    message += "EXAMPLE: /equity/AAPL?start=180530&end=180610<br>"
    message += 'AVAILABLE SYMBOLS:<br>'
    for symbol in  _DATA:
        message += symbol + "<br>\n"
    return message

@app.route( '/equity/<symbol>' )
def returnEqData( symbol ):
    start = request.args.get( 'start' )
    end   = request.args.get( 'end'   )
    
    return rangeAsFix( symbol, start, end )   

if __name__ == "__main__":
    _DATA = loadAllData()
    Flask.run( app, host = '0.0.0.0', port = 8081)
