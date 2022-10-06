#!/bin/bash

x=1

# Generate 200 days old date
while [ $x -le 20 ]
do

        datedl=$(date --date "+$x days ago" "+%-%m-%d")
        zip="$datedl.zip"
        b64=$(echo $zip | base64)
        ok=$(expr $b64 : "\(.*\).$")

        urlbase="https://whoisds.com/whois-database/newly-registered-domains/"
        urlend="=/nr"

        allurl="$urlbase$ok$urlend"

        echo $allul

        wget -O $zip $allurl

        #unzip $zip
x=$(($x+1))
done
