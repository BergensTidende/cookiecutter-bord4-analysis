#!/bin/sh
PROJECTNAME=${PWD##*/}
ANALSYSDIR="${ANALSYSDIR:-/usr/share/nginx/html/analyse/}"
WEBADRESSE=$ANALYSE_URL
CONNECTION=$ANALYSE_CONNECTION
DESTDIR="$ANALSYSDIR$PROJECTNAME"

echo "Kopierer filer til server"
ssh $CONNECTION "mkdir -p $DESTDIR"
scp -r ./report_build/* $CONNECTION:$DESTDIR