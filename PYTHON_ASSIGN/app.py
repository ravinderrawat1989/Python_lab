#!flask/bin/python
from flask import Flask
import json
from ParsingMetacritic import getTopGamesJSON

app = Flask(__name__)

@app.route('/games', methods=['GET'],endpoint='getAllTopGamesJSON')
def getAllTopGamesJSON():
	return getTopGamesJSON()

@app.route('/games/<game_title_input>', methods=['GET'],endpoint='getMatchingTopGameJSON')
def getMatchingTopGameJSON(game_title_input):
	all_games_array=json.loads(getTopGamesJSON())
	for oneJson in all_games_array:
		if oneJson['title'] == game_title_input:
			return oneJson
	return "No Match found"



if __name__ == '__main__':
    app.run(debug=True)

