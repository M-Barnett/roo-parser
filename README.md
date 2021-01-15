# roo_parser
Proof of concept for parsing deliveroo sites for specific options to get some munch

## System Requirements
These are system recommendations, the programme may work on other configurations.</br>
Python 3.9.0</br>
BeautifulSoup 4.9.3

## Installation
`pip install beautifulsoup4`

## Use
The proof of concept is fairly basic, as of January 14, 2021 the use is as follows:

Run the code with the command `python parser.py $WORD`, replacing `$WORD` with
whatever word you want to search for.

The default word is set to "chicken".

To test more values, change or remove the indices where specified.

## Next Steps
* Print values to CSVs
* Separate restaurants by region
* Allow for specific restaurant selection?
* Adjust to find more than just text
