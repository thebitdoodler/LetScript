#/bin/bash


_target=$1

echo "$_target"

assetfinder --subs-only $_target | anew subdomains.txt

#curl "https://crt.sh/?q=$_target&output=json" | jq ".[].name_value" | sed 's/\"//g' | sed 's/\*\.//g' | sort -u > subdomains.txt

#performing port scanning via naabu
naabu -list subdomains.txt -o /tmp/naabu.txt



