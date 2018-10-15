

URL = "https://www.investopedia.com/markets/api/partial/historical/?Symbol=%s&Type=Historical+Prices&Timeframe=Hourly&StartDate=Nov+28%2C+2001&EndDate=Oct+05%2C+2018"

SYMBOL_LIST = [ 'AAPL', 'GOOG', 'TSLA', 'AMZN', 'SHLD' ] 
import urllib



def getData():
	for symbol in SYMBOL_LIST:
		url = URL.replace('%s',  symbol) 
		urllib.urlretrieve( url, 'data/' + symbol )	 

def main():
	pass

if __name__ == "__main__":
	main()


