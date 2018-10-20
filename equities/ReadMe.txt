
*** Requirements

python 
pandas 
flask


*** Getting started

Navigate to the folder containing the file service.py in a terminal.

Run the following command.

>> python service.py 

Go to http:127.0.0.1:8080 in a browser. 

You should see a web page showing the stocks that have available data.

Add "/equity/SYMBOL?start=START_DATE&end=END_DATE" to the end of the URL to fetch the data. 

For view data for AAPL from May 30th, 2018 to June 10th, 2018, the URL would be http:127.0.0.1:8081/equity/AAPL?start=180530&end=180610 


