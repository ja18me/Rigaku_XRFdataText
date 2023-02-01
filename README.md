Rigaku_XRFdataText
====

The script reads the Rigaku CSV files with XRF data and splits and regroups the data based on measured elements. I quick plotting feature is also included to quick verification of the data.

INSTALLATION
----
To use the script, it is advisable to create a python virtual environment and run "py -m pip install -r Library_names.txt" or "pip install -r Library_names.txt" after the environment is activated.

HOW TO RUN THE SCRIPT
---

Please, move the Rigaku CSV files in the 'Raw Data' directory.
Run the script 'main' typinh py main.py.
You will be asked to specific two numbers (columns of the MACCOR text file to work out the average).
You will get the average of charge the discharge values at a given cycle number for multiple cells.

Example
---

Please use the file in Raw Data as an example of how to run the file.\
Try: py main.py -p\
Adding the -p flag will plot the data as the script is reading it.
