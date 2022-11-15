# JAVASCRIPT - Web Scraping

## RESOURCES:books:
Read or watch:
* [Working with JSON data](https://intranet.hbtn.io/rltoken/RmDpb2gJfPrMar05QdxYvw)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.hbtn.io/rltoken/ibqGcS_YNbtWO8nPIlM2Ug)
* [request module](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ)
* [Modern JS](https://intranet.hbtn.io/rltoken/Zf5LCjoTEuIXWWxoH_dGVQ)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

---
## Install request module and use it

[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
---

### [Task 0. Readme](./0-readme.js)
* Write a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
```

### [Task 1. Write me](./1-writeme.js)
* Write a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object
```

### [Task 2. Status code](./2-statuscode.js)
* Write a script that display the status code of a GET request.
* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request
```

### [Task 3. Star wars movie title](./3-starwars_title.js)
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
* You must use the module request
```

### [Task 4. Star wars Wedge Antilles](./4-starwars_count.js)
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the [Star wars API:](https://swapi-api.hbtn.io/api/films/)
* Wedge Antilles is character ID 18
* You must use the module request
```

### [Task 5. Loripsum](./5-request_store.js)
* Write a script that gets the contents of a webpage and stores it in a file.
* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module request
```

### [Task 6. How many completed?](./6-completed_tasks.js)
* Write a script that computes the number of tasks completed by user id.
* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* You must use the module request
```

### [Task 7. Who was playing in this movie?](./100-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line
* You must use the Star wars API
* You must use the module request
```

### [Task 8. Right order](./101-starwars_characters.js)
* Write a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line in the same order of the list “characters” in the /films/ response
* You must use the Star wars API
* You must use the module request
```

### [Task 9. Twitter Auth](./102-search_twitter.js)
* Write a Javascript script that takes in 3 strings and sends a search request to the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index)
* Use the [Twitter API search endpoint](https://developer.twitter.com/en/docs/api-reference-index)
* Use the [Application-only authentication](https://developer.twitter.com/en/docs/authentication/overview) flow to do a search request
* Create an Twitter application [here](https://developer.twitter.com/en/apps)
* The first argument must be the Consumer Key (API Key)
* The second argument must be the Consumer Secret (API Secret)
* The third argument must be the search string
* Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
* Only these modules are allowed: request, base-64 and utf8
* You don’t need to check arguments passed to the script (number or type) 
```
---
## Author
* **Bello Abayomi** - [BluvD143](https://github.com/BluvD143)
