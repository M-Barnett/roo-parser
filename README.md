# roo_parser
Proof of concept for parsing deliveroo sites for specific options to get some munch.

## System Requirements
These are system recommendations, the programme may work on other configurations.</br>


_Python 3.9.0_</br>
_BeautifulSoup 4.9.3_

## Installation
All packages not mentioned here should be included in Python 3.</br>

Install the BeautifulSoup package (Python 3) for parsing the html.</br>
`pip3 install beautifulsoup4`

## Use
The proof of concept is fairly basic, as of January 15, 2021 the use is as follows:

### Default Run
Command: `python parser.py` </br>
</br>
_N.B._ if your python command is not mapped to Python 3 you may
need to instead use the command `python3`</br>

### Additional Arguments
**Word**</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Command: `python parser.py $WORD`</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$WORD` with the word you want to search for.</br>

**CSV Name**</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Comand: `python parser.py $WORD $CSV_NAME`</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$WORD` with the word you want to search for.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$CSV_NAME` with the name of the file you want to save to.</br>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _N.B._ The `$CSV_NAME` should be a simple string, the code will add ".csv" to
the end of it.
</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; As of January 15, 2020 you must have a `$WORD` argument to have a
`$CSV_NAME` argument, but this should hopefully be changed soon.

### Output
The code is currently limited to only parse a few pages for efficient testing,
to test more values, change or remove the indices in the `restaurant_checker`
function in `parser.py` where specified (line 41).

The code writes the results to a csv file with Name and a Boolean fields
displaying whether or not the word was found for a given restaurant. 

## Next Steps
* Add flagging for arguments so `$CSV_NAME`can be specified without `$WORD`
* Separate restaurants by region
* Allow for specific restaurant selection?
* Adjust to find more than just text
