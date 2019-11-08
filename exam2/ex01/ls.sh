#!/bin/bash

ls -l >> /tmp/ls.log
echo //etc/passwd "ls ok"

#le script doit afficher la sortie d'erreur vers un fichier /tmp/ls_err.log
ls -l /etc/passwd || echo "ls erreur" >> /tmp/ls_err.log


#le script doit afficher si le ls a fonctionné (c'est-a-dire l'exit code)
ls -l
if [ "$?" -ne "0" ]; then
  echo "ls FAIL"
  exit 1
fi
