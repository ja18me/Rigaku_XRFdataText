# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 17:15:57 2022

@author: Menon_A, Paez_G
"""

import os
import sys
import argparse
import XRFdataUtilities as xrfU

directoryName=xrfU.directoryName
ImgDirectory=xrfU.ImagesDirectory

parser = argparse.ArgumentParser(description='Preprocessing and quickly plotting XRF Data',epilog='Default: %(prog)s restructure the original data for further analysis')
parser.add_argument('-p','--PlotYes', action='store_true', help='data restructuring and plotting for new runs, activate the plotting feature if needed for runs already done')
parser.add_argument('-v','--version', action='version', version='XRFplotting 0.1')

args=parser.parse_args()

#Makes sure the data directory is created 
ifExistDirectory = os.path.exists("./"+directoryName)
if not(ifExistDirectory):
    print("Directory "+directoryName+" does not exist")
    os.mkdir("./"+directoryName)
    print("Directory "+directoryName+" has been created")
    print("Please move the CVS files to restructure the data")
    sys.exit()

#Makes sure the Datadirectory is not empty
files=os.listdir("./"+directoryName)
if len(files)==0:
    print(directoryName+" is empty")
    print("Please move the CVS files to restructure the data")
    sys.exit()

if not(args.PlotYes):
    list_subfolders = [f.name for f in os.scandir("./"+directoryName) if f.is_dir()]
    if len(list_subfolders)>0:
        print("There is a previous run in the "+directoryName+" Directory")
        print("Please move the old files to continue")
        sys.exit()

    xrfU.DataReStructure(files)
else:
    list_subfolders = [f.name for f in os.scandir("./"+directoryName) if f.is_dir()]
    if (ImgDirectory in list_subfolders):
        print("The images of the data were alredy created")
        print("Please go to "+ImgDirectory+" in the "+directoryName+" Directory to find them")
        sys.exit()

    if len(list_subfolders)==0:
        xrfU.DataReStructure(files)
        xrfU.QuickPlotting()
    else:
        xrfU.QuickPlotting()
        
