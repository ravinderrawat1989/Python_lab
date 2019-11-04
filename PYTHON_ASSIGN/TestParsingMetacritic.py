import unittest
import requests 

class TestParsingMetacritic(unittest.TestCase):

#This returns list of all games on website viz 10
    def test_all_games(self):
	URL = "http://localhost:5000/games"
	response=requests.get(url = URL)
        self.assertEqual( len( response.json()  ) , 10)

#This looks for correct specific Game's name.
    def test_specific_game(self):
        URL = "http://localhost:5000/games/The Outer Worlds"
        response=requests.get(url = URL)
        self.assertEqual(  response.json()['title'] , 'The Outer Worlds')
	self.assertEqual(  len(response.json()) ,2)

#Put dummy game name to be searched and fail
    def test_specific_game_missed(self):
        URL = "http://localhost:5000/games/WRONG_DUMMY"
        response=requests.get(url = URL)
        self.assertEqual(  response.text , 'No Match found')

if __name__ == '__main__':
    unittest.main()
