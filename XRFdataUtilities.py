# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 17:15:57 2022

@author: Menon_A, Paez_G
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

###########-----------Constants----------------###########
plt.style.use('seaborn-paper')
plt.rc('font',family='Arial')
directoryName="RawData"
ImagesDirectory="QuickImages"
constant_Angle_ev=6.19920974479022*pow(10,3) #Planck*speedOflight/2 [eV*Angstroms]
PI=3.141592654
Dspacing={ #in angstroms
    "Al-KA": 4.371, #PET /2
    "B -KA": 100, #RX80 /2
    "C -KA": 80, #RX61 /2
    "Ca-KA": 2.0135, #LiF 200
    "Cl-KA": 3.2645, #Ge /2
    "F -KA": 15, #RX25 /2
    "Heavy(1)": 2.0135, #LiF 200
    "Heavy": 2.0135, #LiF 200
    "K -KA": 2.0135, #LiF 200
    "Mg-KA": 15, #RX25 /2
    "N -KA": 55, #RX45 /2
    "Na-KA": 15, #RX25 /2
    "O -KA": 27.5, #RX35 /2
    "P -KA": 3.2645, #Ge /2
    "S -KA": 3.2645, #Ge /2
    "Si-KA": 4.371 #PET /2
    }
###########-----------Constants----------------###########

def ExportingData(DF,RName,Fname):
    FileAdress="./"+directoryName+"/"+Fname[:-4]
    if not os.path.exists(FileAdress):
        os.mkdir(FileAdress)
    DF.to_csv(FileAdress+"/"+Fname[:-4]+"_"+str(RName)+".csv", index=False)

def Splitting(DF,FileName):
    DF['group'] = DF.isnull().all(axis=1).cumsum()
    RegionNumbers=DF.group.max()
    for i in range(RegionNumbers+1):
        DF_data=pd.DataFrame()
        if i==0:
            region = DF[DF['group']==i].iloc[0,0]
            DF_data['energy'] = DF[DF['group']==i].iloc[1: , 1]
            DF_data['intensity'] = DF[DF['group']==i].iloc[1: , 2]
        else:    
            region = DF[DF['group']==i].iloc[1,0]
            DF_data['energy'] = DF[DF['group']==i].iloc[2: , 1]
            DF_data['intensity'] = DF[DF['group']==i].iloc[2: , 2]
        DF_data=DF_data._convert(numeric=True)
        DF_data['energy']=constant_Angle_ev/Dspacing[region]/np.sin(DF_data['energy']*PI/180/2)
        DF_data=DF_data.sort_values(by=['energy'])
        ExportingData(DF_data,region,FileName)
        del DF_data

def QuickPlotting():
    Paths=os.listdir("./"+directoryName)
    DirectoryPaths=[] #List of directories where to look for regions to plot
    for pfile in Paths:
        if os.path.isfile("./"+directoryName+"/"+pfile):
            continue
        DirectoryPaths.append(pfile)

    Regions=[] #List of Regions to plot
    for x in DirectoryPaths:
        files=os.listdir("./"+directoryName+"/"+x)
        for f in files:
            reg=f[len(x)+1:-4]
            if not(reg in Regions):
                Regions.append(reg)

    if not os.path.exists("./"+directoryName+"/"+ImagesDirectory):
        os.mkdir("./"+directoryName+"/"+ImagesDirectory)
    for r in Regions:
        fig = plt.figure()
        axes=fig.add_subplot(1,1,1)
        for d in DirectoryPaths:
            try:
                df_plot = pd.read_csv("./"+directoryName+"/"+d+"/"+d+"_"+r+".csv", usecols=(0,1))
            except FileNotFoundError:
                continue
            axes.plot(df_plot['energy'],df_plot['intensity'], label=d)
            del df_plot
            axes.legend(loc ="upper left")
            if r=='Heavy':
                axes.set_yscale('log')
                axes.legend(loc ="lower right")
                plt.xlim([4000,18000])
        axes.set_xlabel('Emission energy (eV)')
        axes.set_ylabel('Intensity (arb. units)')
        fig.suptitle(r, fontsize=16)
        fig.savefig("./"+directoryName+"/"+ImagesDirectory+"/"+r+'.png', dpi=300, facecolor = 'w')

def DataReStructure(Files):
    for x in Files:
        if x[-3:]!='csv':
            next
        else:
            df = pd.read_csv("./"+directoryName+"/"+x, usecols=(1,2,3), header=None)
            Splitting(df,x)
    

#def SaveToFile(Energy,Signal,RunName,ExpName):
#    with open(directoryName+"/"+RunName[0:-4]+"_"+ExpName+".txt","w") as txt_file:
#        txt_file.write("#"+RunName[0:-4]+" "+ExpName+"\n")
#        txt_file.write("#Energy"+"\t"+"Spectrum\n")
#        for i in range(len(Energy[0])):
#            txt_file.write("".join(str(Energy[0][i]))+"\t"+"".join(str(Signal[0][i]))+"\n")
        
