#/bin/bash

# Fetching domains from crt.sh
_target=$1

echo "$_target"
curl "https://crt.sh/?q=$_target&output=json" | jq ".[].name_value" | sed 's/\"//g' | sed 's/\*\.//g' | sort -u 

#naabu -host $_target  -o /$_target_naabuScan.txt

