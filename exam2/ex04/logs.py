#!/usr/bin/python3

from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y %H:%M:%S")

fichier = open("python.log", "a")
fichier.write(str(date_time))
fichier.close()
