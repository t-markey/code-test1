###	tasks
1. DONEpull repo
2. DONEget up and running
```
$ export FLASK_APP=hello.py
$ flask run
```
3. DONEfix 'The back-end contain several errors'
4. DONEform for searching
5. DONEhit api test
6. show results
7. each result goes to dynamic info page
8. user be able to save favorites
9. DONElink to page of favorites movies
10. STARTEDadd bootstrap?
11. test running on phone
12. edge case search results
13. Make carousel with posters
14. Have carousel be 3 random posters












### GOAL 

> Create a webpage that will utilize an external API to request movie data.
The webpage will be served by a back-end which will have the ability to persist data.

#### Back-end Instructions

- Within this repo you will find a flask api (`app.py`).

- The back-end contain several errors,
so you will need to do some debugging to ensure it is working correctly.

- The page should have a form that allows visitors to search.
- the api uses the [OMDBapi](http://www.omdbapi.com/)
to search for matching movies and then display the results.
 - *Example*: If a user searches for `Star Wars`, a list of every Star Wars movie will be displayed.

- When the user clicks on a search result display detailed information about that movie in a new page.
- *Example*: If a user is viewing a list of every Star Wars movie and clicks on `Star Wars: A New Hope`,
the browser opens a new page with information about that specific movie.

- Users should be able to "favorite" a movie and have it persisted via the provided back-end.

- Provide a link to display favorited movies.

- Add bootstrap 4 and make sure the app works well on your phone.

- The app should handle edgecases like searching for "   star  " or "blade run".

#### Things we are looking for

- Clear, simple code
- Explanatory comments
- Consistent Naming Conventions
- Valid HTML, CSS, Python, and JavaScript
- Proper handling of edge-cases. You should try to break the website and fix any issues before submitting it.

#### Deliverables

- Please send us back a link to a git repo with the completed code challenge. 

- Include a README.md file in your repo with a link to your application deployed on Heroku or any cloud provider.
