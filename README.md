# Gibberish

## What is Gibberish?

Gibberish is the made used for the Soundex algorithm which is a phonetic algorithm for indexing names by sound. Soundex aims to encode characters to be homonyms with minor differences in spelling.

## How to Run Gibberish Generator

`python3 gibberish_generator.py -w <word>`

-w: word to generate gibberish

## Example

`python3 gibberish_generator.py -w "Computer Science"`

## How to contribute

1) Generate new gibberish word using `gibberish_generator.py` or think by your own
2) Add that word to `gibberish.csv`
3) Run `update_data.py` to update JSON file
4) Open pull request to base repository