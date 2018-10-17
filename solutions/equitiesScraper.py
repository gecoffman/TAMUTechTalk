from requests import get
from datetime import date

SYMS = [ 'AAPL', 'GOOG', 'AMZN', 'TSLA', 'SHLD' ]

def fetchSymbolData( sym ):
    ''' return raw data from a call to the equity service, for the given symbol '''
    url = 'http://localhost:8081/equity/' + sym + '?start=%s&end=%s' % ( date( 1970,1,1 ).strftime('%y%m%d'), date.today().strftime('%y%m%d') )
    response = get( url )
    return response.text

def main():
    for sym in SYMS:
        with open( sym + '.csv', 'w' ) as handle:
            handle.write( fetchSymbolData( sym ) )
            
if __name__ == '__main__':
    main()
