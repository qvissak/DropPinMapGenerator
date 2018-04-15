# Drop Pin Map Generator
Given a CSV of comma separated points per row, generates an html file using the gmplot library of a map with multi-colored drop pins representing each point.

## Setup
Set up on Mac or Linux. To install on Windows, follow instructions from [Python's website](https://www.python.org/downloads/). Be sure to set your environment variables appropriately. Installation of gmplot on windows should be the same command.
```sh
$ sudo apt install python3
$ sudo apt install pip3
$ pip3 install gmplot
```

## To Run
Please include the file extension for your csv. Ensure your csv is in the proper format (1 point per row, separated by a single comma). Do not include the file extension for the output file name.
```sh
$ python3 ./input.py <filename.csv> <output-file-name>
```

## Output
Open the html file generated in your web browser to view map.
`<output-file-name>.html`

### Example
```sh
$ python3 ./input.py inputExample.csv outputExample
```
