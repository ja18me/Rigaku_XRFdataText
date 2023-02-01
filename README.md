Rigaku_XRFdataText
====

The script reads the Rigaku CSV files with XRF data and splits and regroups the data based on measured elements. A plotting feature is also included to quick verification of the data.

INSTALLATION
----
To use the script, it is advisable to create a python virtual environment and run "py -m pip install -r Library_names.txt" or "pip install -r Library_names.txt" after the environment is activated.

HOW TO RUN THE SCRIPT
---
+ Please, move the Rigaku CSV files in the 'Raw Data' directory.
+ Run the script 'main' typing "py main.py".

Example
---

Please use the file in Raw Data as an example of how to run the file.\
Try: py main.py -p\
Adding the -p flag will plot the data as the script is reading it.
