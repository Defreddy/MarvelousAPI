# All imports needed for the API program to work
import hashlib
import requests
import time
import json
from tabulate import tabulate
import pandas as pd
import warnings
import numpy as np
import time

# Put out warnings and set column width for printing data
warnings.filterwarnings("ignore")
pd.set_option('max_colwidth',500)

# Beginning of the API connection program
key = hashlib.md5()
ts = str(time.time())
key_byte = bytes(ts,'utf8')
key.update(key_byte)

# Insert private key:
key.update(b"my_privet_key")

# Insert public key:
key.update(b"my_public_key")

hash=key.hexdigest()
url = "https://gateway.marvel.com"

# Insert public key again:
api_key =  "my_public_key"

# You can change search variables here, but this program is designed for the characters !!
search = "/v1/public/characters" + "?"

# Ask for input
character = input("Enter your character:")
print('\n\n')
name = character

# The final URL used to connect to the Marvel API:
final_url = url + search + "ts=" + ts + "&apikey=" + api_key + "&hash=" + hash +  "&name=" + name

resp = requests.get(final_url, verify = False)
respADV = resp.json()

# This will create a new dict with certain items you need (instead of looking for every single item)
def new_dict(a):
	b = {}
	for key, value in a.items():
		b[key] = value
	return b;

# This will specifically take all names (look fer key "Name" and add values to it)
def dict_name(a):
	b = {}
	d = []
	c = 1
	for x in a:
		names = x['name']
		d.append(c)
		b[c] = names
		c+=1
	return b;

# This will combine the type and name of certain results:
def dict_type(a):
	b = {}
	for x in a:
		types = x['type']
		names = x['name']
		b[names] = types
	return b;

# This will combine the URL and the type of URL:
def dict_url(a):
	b = {}
	for x in a:
		url = x['url']
		types = x['type']
		b[types] = url
	return b;

# Specifically selects the primary details of a character:
def primary_values(a):
	b = {}
	for key, value in a.items():
		id = a["id"]
		b.update({"id":id})
		name = a["name"]
		b.update({"name":name})
		modified = a["modified"]
		b.update({"modified":modified})
	return b;

# Search for suggestions, MAX 20!!
def suggestions():
	x = 0
	data_results = data['data']['results'][x]
	b = {}
	d = []
	c = 0
	count = data['data']['count']
	for i in range(count):
		data_results = data['data']['results'][x]
		names = data_results["name"]
		b[c] = names
		x+=1
		c+=1
	return b
	b = {};

# Primary data from Marvel
data = new_dict(respADV)

# Error handling in case of status codes and non-existing characters:

#print(resp.status_code)
status = resp.status_code

if status == 200:
	print("Your request is succesfull. Welcome to the Marvel Library!")
	print("Connection is stable and you are ready to look for characters!")
	print("\n")
	time.sleep(2)

if status == 401:
	print("Your request has been denied.")
	print("You do not belong here villain!")
	print("Check your credentials: API keys (private and public)")
	print("\n")
	time.sleep(2)

if status == 403:
	print("Your request has been denied.")
	print("You do not have enough rights to open the gates to the Marvel Library")
	time.sleep(2)

if status >= 500:
	print("The Marvel Library is closed at the moment. Please return shortly!")
	time.sleep(2)

# This is a loop that itterates through the input validation. No valid input? Try again!
# You will get a suggestions tab to choose a new option.
# Unfortunately the second faulty try will cause an error which renders the suggestions "uncallable".
# I am guessing the program calls for suggestions() which is incorrect; as a "dict" is called by using []
# This is currently the only "bug" in the entire program.

while True:
	data_empty = data["data"]["total"]
	if data_empty == 0:
		suggestion_url = url + search + "ts=" + ts + "&apikey=" + api_key + "&hash=" + hash +  "&nameStartsWith=" + name
		resp = requests.get(suggestion_url, verify = False)
		respADV = resp.json()
		data = new_dict(respADV)
		print("\n")
		print("Here are some suggestions we found for you:")
		print("\n")
		suggestions = suggestions()
		sug = pd.DataFrame.from_dict(suggestions,orient='index',columns=['Suggestions'])
		print(tabulate(sug, showindex=False, headers=sug.columns))
		print("\n")
		print("The character you entered does not exist, please enter a new character")
		print("\n")
		character = input("Enter your character:")
		print('\n\n')
		name = character
		final_url = url + search + "ts=" + ts + "&apikey=" + api_key + "&hash=" + hash +  "&name=" + name
		resp = requests.get(final_url, verify = False)
		respADV = resp.json()
		data = new_dict(respADV)
	else:
		print("\n\n")
		print("This is a valid character!")
		print("\n")
		print("Loading data...")
		print("\n\n")
		time.sleep(3)
		break;

# Continue if data is found:
data_results = data['data']['results'][0]
results = new_dict(data_results)



# First print of values found for input; table and description
values = primary_values(results)
df = pd.DataFrame.from_dict(values,orient='index',columns=['Data'])

detailname = results['name']
print("Details about " + detailname + " :")
print(tabulate(df, headers=df.columns))
print('\n')
print("Description:")
print('\n')
print(results["description"])

# Data for "comics"
data_comics = results['comics']
comics = new_dict(data_comics)

data_comics_items  = comics['items']
comics_name= dict_name(data_comics_items)


#print(comics_name)
print('\n\n')
com = pd.DataFrame.from_dict(comics_name,orient='index', columns=['Comics'])
print(tabulate(com, showindex=False, headers=com.columns))


# Data for "series"
data_series = results['series']
series = new_dict(data_series)

data_series_items = series['items']
series_name = dict_name(data_series_items)

#print(series_name)
print('\n\n')
ser = pd.DataFrame.from_dict(series_name,orient='index',columns=['Series'])
print(tabulate(ser, showindex=False, headers=ser.columns))

# Data for "stories"
data_stories = results['stories']
stories = new_dict(data_stories)

data_stories_items = stories['items']
stories_type = dict_type(data_stories_items)

#print(stories_name)
print('\n\n')
stoty = pd.DataFrame.from_dict(stories_type,orient='index',columns=['Story type'])
print("Stories:")
print(tabulate(stoty, headers=stoty.columns))

# Data for "events"
data_events = results['events']
events = new_dict(data_events)

data_events_items = events['items']
events_name = dict_name(data_events_items)


#print(events_name)
print('\n\n')
events = pd.DataFrame.from_dict(events_name,orient='index',columns=['Events'])
print(tabulate(events, showindex=False, headers=events.columns))


# Data for "url"
data_url = results['urls']

urls_url = dict_url(data_url)


#print(urls_type)
print('\n\n')
urlt = pd.DataFrame.from_dict(urls_url,orient='index',columns=['URL'])
print("Kind of URL:")
print(tabulate(urlt, headers=urlt.columns))


#Marvel COpyright ;)
print('\n\n')
copyright = data["attributionText"]
print(copyright)