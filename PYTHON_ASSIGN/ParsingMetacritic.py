import requests
import urllib
import json
from bs4 import BeautifulSoup

url = 'https://www.metacritic.com/game/playstation-4/'

def getTopGamesJSON():
	# Connect to the URL
	headers = {'User-Agent': 'Dummy'}
	response = requests.get(url,headers=headers)

	# Parse HTML and save to BeautifulSoup object
	soup = BeautifulSoup(response.text, "html.parser")

	metascoreList = []
	all_metaScoreDiv = soup.find_all("div",{"class":"clamp-metascore"})
	for metaDiv in all_metaScoreDiv:
		children = metaDiv.findChildren("div" , { "class" : "metascore_w large game positive"})
		for child in children:
			metascoreList.append(int(child.text))
      
	#print metascoreList
	titleList = []
	all_titleDiv = soup.find_all("a",{"class":"title"})
	for titleDiv in all_titleDiv:
		children = titleDiv.findChildren("h3")
		for child in children:
			titleList.append(child.text.rstrip().lstrip())
      
      
	title_with_score = [{"title" : title , "score" : score } for title,score in  zip(titleList,metascoreList)] 
	return json.dumps(title_with_score,indent=2,sort_keys=False)




