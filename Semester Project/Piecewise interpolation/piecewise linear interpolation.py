#! /usr/bin/env python3
#! /usr/bin/env python3

from re import I
import sys

from parse_temps import (parse_raw_temps)

def polate(x,y):
    with open('inter.txt','w+') as interpol:
        b=[];
        m=[];
        for i in range(len(x)-1):
            m.append((y[i+1]-y[i])/(x[i+1]-x[i]));
            b.append(y[i]-(m[i]*x[i]));
            interpol.write("      "+str(x[i])+" <= x <      "+str(x[i+1])+"; y_"+str(i)+"      =      "+str(b[i])+" +   "+str(m[i])+"x; interpolation\n");
    interpol.close()

        
        
    

def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    input_temps = "sensors-2018.12.26-no-labels.txt"


    with open(input_temps, 'r') as temps_file:
        # ----------------------------------------------------------------------
        # Split Data
        # ----------------------------------------------------------------------
        times = []
        core_0_data = []
        core_1_data = []
        core_2_data = []
        core_3_data = []
        for time, core_data in parse_raw_temps(temps_file):
            times.append(time)
            core_0_data.append(core_data[0])
            core_1_data.append(core_data[1])
            core_2_data.append(core_data[2])
            core_3_data.append(core_data[3])

    polate(times,core_0_data);
        

if __name__ == "__main__":

    main()