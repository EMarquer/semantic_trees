Description
Method for NLP project

## Files
* `toy_corpus/`: folder where the toy corpus data is located
  * `xml/`: folder where the XML version of the definitions are located
    * `carrot.xml`: XML of the definition of the noun "carrot", source is [the article "carrot" of the McMillan Dictionnary](https://www.macmillandictionary.com/dictionary/british/carrot)
    * `sweet_1.xml`: XML of the definition of the adjective "sweet", source is [the article "sweet_1" of the McMillan Dictionnary](https://www.macmillandictionary.com/dictionary/british/sweet_1)
* `data/`: folder where the data produced by the different scripts is stored
  * `xml/`: folder where the XML version of the definitions are located; produced by `extract_xml.py`
* `extract_xml.py`: script to build a XML representation of a word definition given its dictionary key (like "sweet_1" or "carrot") or the URL of the definition; later on, support for word search should be included, but for now it is necessary to provide the URLs or dictionary keys; the produced XML is stored under `data/xml`
* `extract_xml_test.py`: unit tests for `extract_xml.py`
* `dictionary_scrapping.py`: script to extract a definition given its dictionary key (like "sweet_1" or "carrot") or the URL of the definition; later on, support for word search should be included, but for now it is necessary to provide the URLs or dictionary keys; the produced XML is stored under `data/xml`
* `dictionary_scrapping_test.py`: unit tests for `extract_xml.py`

## Setup & Dependencies
This project is built using Python >= 3.6

The following packages are needed:
* `lxml` (see https://stackoverflow.com/a/19940637)
* `bs4`

## Theoretical basis
### Distance between ordered trees
* https://www.ifi.uzh.ch/dbtg/teaching/thesesarch/Vertiefung_LeaBay_v2.pdf
* https://arxiv.org/abs/1508.03381
* [https://doi.org/10.1007/978-3-642-22194-1_71](https://sci-hub.tw/https://doi.org/10.1007/978-3-642-22194-1_71)

### Distance between unordered trees
* [https://ieeexplore.ieee.org/document/6630333](https://sci-hub.tw/https://ieeexplore.ieee.org/document/6630333]
* [https://ieeexplore.ieee.org/document/1260818](https://sci-hub.tw/https://ieeexplore.ieee.org/document/1260818)

## References
