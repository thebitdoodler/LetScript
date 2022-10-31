#/bin/bash


_target=$1

#echo "$_target"

# Finding alive sub-domains
 
mkdir -p $_target

cd $_target

assetfinder --subs-only $_target | httpx | anew $_target_subdomains.txt

curl "https://crt.sh/?q=$_target&output=json" | jq ".[].name_value" | sed 's/\"//g' | sed 's/\*\.//g' | sort -u > $_target_subdomains_crtsh.txt

#performing port scanning via naabu
naabu -list subdomains.txt -o /tmp/naabu.txt

# Performing a nuclei vulnerability scan for initial recon and low-hanging bugs check
nuclei -l $_target_subdomains.txt -t ~/nuclei-template
