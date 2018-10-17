from requests import get

PAIRS = [ 'AUDUSD', 'EURUSD', 'GBPUSD', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDJPY' ]

def fetchForexPair( pair ):
    ''' return raw data from a call to the forex service, for the given pair '''
    url = 'http://localhost:8080/forex/' + pair
    response = get( url )
    return response.text

def main():
    for pair in PAIRS:
        with open( pair + '.json', 'w' ) as handle:
            handle.write( fetchForexPair( pair ) )
            
if __name__ == '__main__':
    main()