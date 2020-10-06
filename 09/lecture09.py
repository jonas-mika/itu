a#lecture09

###################
# basic dictionary examples
###################
capitals = {'France': 'Paris', 
'England': 'London', 
'Denmark': 'Copenhagen', 
'Sweden': 'Stockholm'}

{}
capitals.pop("Norway")
capital.values()

#loops:
for i in capitals.items():
    print(i)

other_capitals = {"Norway": "Oslo", "Bulgaria": "Sofia"}
capitals.update(other_capitals)

#nested
what2wear = {}
monday = {"jacket":True, "shoes":"runners", "temp":11}
what2wear["monday"]=monday
tuesday = {"jacket":False, "shoes":"sandals", "temp":21}
what2wear["tuesday"]=tuesday

#look up
what2wear['monday']
what2wear['monday']['shoes']
###################
# dictionary comprehensions
###################
r = [2*x for x in range(50)]
d = {i: [] for i in r }

###################
#read csv into dictionary
###################
import csv
with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)

#output
{'Name': 'Jack', ' Age': ' 23', ' Profession': ' Doctor'}
{'Name': 'Lucy', ' Age': ' 22', ' Profession': ' Engineer'}
######################
#
#######################
# Python program to demonstrate 
# Conversion of JSON data to 
# dictionary 
#https://jsonformatter.org/html-viewer
  
  
# importing the module 
import json
  
# Opening JSON file 
with open('example.json') as json_file: 
    data = json.load(json_file) 
  
    # Print the type of data variable 
    print("Type:", type(data)) 
  
    # Print the data of dictionary 
    for person in data["employees"]:
    	print(person["firstName"])

      

##################
#
##################
#import html from webpage like last time
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

url='https://www.thedanishparliament.dk/en/political-parties'
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')


#install bs4 first
import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
#try it out:
print(soup.h2)
print(soup.head)

root = soup.body
root_childs = [e.name for e in root.children if e.name is not None]
print(root_childs)

root_childs = [e.name for e in root.descendants if e.name is not None]
print(root_childs)

#find the list of political parties
#use a regex to find the right node
node = soup.find("h2", string=re.compile("Political Parties.*"))

parties = node.findNextSibling()
links = parties.findAll("a")

for p in links:
	print(p.text)
	print(p.get("href"))

#create dictionary to store as JSON file
data = {
  "parties": [
    {
	 "name": p.text,
	 "link": p.get("href")
	}
	for p in links	
			]
}

with open('outfile.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('outfile.json') as json_file: 
    data = json.load(json_file)    







