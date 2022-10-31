#/bin/bash

_target=$1

#echo "$_target"

# Making target directory
 
mkdir -p $_target

# Shifting to the target directory
cd $_target

assetfinder --subs-only $_target | httpx | anew subdomains.txt


# Performing a curl lookup onto crt.sh domain to fetch JSON body of sub-domains for given domains
curl "https://crt.sh/?q=$_target&output=json" | jq ".[].name_value" | sed 's/\"//g' | sed 's/\*\.//g' | sort -u > subdomains.txt

#performing port scanning via naabu
naabu -list subdomains.txt -o /tmp/naabu.txt
