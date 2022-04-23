# Currency-Alert

### Steps to run:
First install the dependencies:

`pip install -r requirements.txt`

Then run the program using python:

`py __main__.py`

It will ask for a jsonline file populated with currency exchange rates in the following format:\
You can use example files input1.jsonl or input2.jsonl

> { "timestamp": 1554933784.023, "currencyPair": "SYPAUD", "rate": 0.39281 }
>  
This defines a spot price of Syrian Pound -> to Australian Dollar at a rate of 0.39281

It will then give you a list of what currency's exchange rate has changed +10%/-10% compared to its rolling 5 minute average.\
This is useful in determining erratic forex changes.

### How it works

Dependencies:

>Jsonlines: reads jsonline files.
>
>Pandas, numpy: used to obtain rolling average.

<img src="https://github.com/jacobelali3/Currency-Alert/blob/master/UML.png" alt="UML diagram" width="200"/> <img src="https://github.com/jacobelali3/Currency-Alert/blob/master/TestRun.PNG" alt="Example test run" width="600"/>


