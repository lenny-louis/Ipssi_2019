import sys
import time
import os

def show_sla(d):
    ind=3600*24*365.25*(1-(d/100))
    #99.9 = 31557, convertir
    resultatcalcul = time.strftime('%Hh %Mm %Ss', time.gmtime(ind))
    return resultatcalcul

if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))