#!/bin/bash

ls -l >> /tmp/ls.log
echo "ls ok"

#le script doit afficher la sortie d'erreur vers un fichier /tmp/ls_err.log
ls -l || echo "Je n'ai pas de fichier foo." >> /tmp/ls_err.log


#le script doit afficher si le ls a fonctionné (c'est-a-dire l'exit code)
ls -l
if [ "$?" -ne "0" ]; then
  echo "Sorry, cannot find user ${1} in /etc/passwd"
  exit 1
fi
