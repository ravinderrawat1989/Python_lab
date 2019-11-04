This utility aims at scaping data from www.metacritic.com.
It solely aims for 'Top Playstation 4 Games' listed on the website.


About : -
Utility has base directory PYTHON_ASSIGN ,which consists of two main files listed below:-

1). ParsingMetacritic.py is the file that contains function to read website and get a JSON styled list of top Games 
	from the website www.metacritic.com.
 		- It uses BeautifulSoup python package for parsing HTML page.
 			
2). app.py - This is the main File which will be invoked.
		- It uses Flask Web framework viz is a Simple yet powerful Python web framework.
		- By default Flask comes up on port 5000 ,against which GET request can be triggered.
		


Pre-requisites:- 
1). If Flask is not installed on your system, execute below command 
     --------------
	$ virtualenv flask
	$ flask/bin/pip install flask     		
     --------------     

2).  If BeautifulSoup package is not installed on your system, execute below command
     --------------
	$ pip install BeautifulSoup    		
     --------------     

3). Validate if website URL is correct viz is as variable ,url,specified in the file ParsingMetacritic.py.



Steps to execute :- 
1). change directory to PYTHON_ASSIGN.
2). Run below command to bring up the Flash server on default port 5000.
     --------------     
     $ python app.py 
     --------------                    	
3). Open a browser(Client) or use basic Curl command Line tool to get desired output:
	
	For instance :-
	
	a). Fetch all Game List: - 
		 Browser - http://localhost:5000/games 
	 	 Curl    - curl http://localhost:5000/games
		
	b). Fetch a specific Game detail: - 
		Browser - http://localhost:5000/games/<NAME OF THE GAME>
		Curl    - curl http://localhost:5000/games/<NAME OF THE GAME>


		
FAQ :-
1). If name of game being searched has spaces,then while using CURL replace the SPACE with '%20'.
2). If the specific game is not present in top Games list ,then 'No Match found' is returned.
3). To Stop Flask Server use 'ctrl + c'.
4). Use TestParsingMetacritic.py to perform some rounds of Unit Testing for the utility.
	Use below command to trigger - 
     --------------     
     $ python TestParsingMetacritic.py
     --------------          	
	