## Description
Method for NLP project

## Files
* `toy_corpus`: folder where the toy corpus data is located
  * `xml`: folder where the XML version of the definitions are located
    * `carrot.xml`: XML of the definition of the noun "carrot", source is [the article "carrot" of the McMillan Dictionnary](https://www.macmillandictionary.com/dictionary/british/carrot)
    * `sweet_1.xml`: XML of the definition of the adjective "sweet", source is [the article "sweet_1" of the McMillan Dictionnary](https://www.macmillandictionary.com/dictionary/british/sweet_1)
* `data`: folder where the data produced by the different scripts is stored
  * `xml`: folder where the XML version of the definitions are located; produced by `extract_xml.py`
* `extract_xml.py`: script to extract and build a XML representation of a word definition given its dictionary key (like "sweet_1" or "carrot") or the URL of the definition; later on, support for word search should be included, but for now it is necessary to provide the URLs or dictionary keys; the produced XML is stored under `data/xml`
* `extract_xml_test.py`: unit tests for `extract_xml.py`

## Setup & Dependencies
This project is built using Python >= 3.6

The following packages are needed:
* ???
* ???

## Theorical basis

## References
