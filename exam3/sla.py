import sys
import time
from math import floor

def show_sla(disponibilite):
    indispo=3600*24*365.25*(1-(disponibilite/100))
    h = (int(indispo // 3600))
    m = indispo % 3600 // 60
    s = indispo % 3600 % 60 // 1

    return ("{}h {}m {}s".format(h, floor(m),s))


if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))
