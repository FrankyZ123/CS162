## Making HTTP requests
This pre-class work can be quite long if you have had no previous exposure to
HTML and web programming.  In this case you are encouraged to find someone with
some prior experience and work together.  (Conversely, if you do have any prior
experience, then you are encouraged to find someone with no web experience to
help them!)

### HTML Forms
The first time that you usually encounter an HTML request (other than a GET
request) is in an HTML form.  The following (freely-available) short course uses
active learning to help you understand HTML forms:
https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms

For this session you will need to work through the following guides:
1. Your first HTML form
2. How to structure an HTML form
3. The native form widgets
4. Sending form data

After which you should feel comfortable tackling question 1.

### Python HTTP requests
However, we can also query the web through a python program.  There are many
ways of making http requests programmatically.  A nice library is the `requests`
library.  You can install it using:
```python3
pip3 install requests
```
Now work through [the guide to HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview).

And then read through the [quickstart for python requests](http://docs.python-requests.org/en/master/user/quickstart/).

### JSON
The web services listed below all return information in a format known as JSON.
Fortunately for us it is straightforward to turn the JSON back into standard
python objects that you are already familiar with.

As an example (borrowed from the requests tutorial), here is a call to github,
which is then read into a python list of python dictionaries:
```python3
>>> import requests
>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

### 1. Kanban form

Build on your work from the previous session in which you designed a basic
Kanban website. For today's class you need to build a small HTML form which
will allow you to write a short description of the task which you want to add
to the board.

### 2. Pokemon

Here is an example link to return Pokemon data in JSON format (https://pokeapi.co/api/v2/pokemon/charmeleon). You can see the documentation of Pokemon API at https://pokeapi.co/docs/v2.html.

Choose your favorite Pokemon, and write a short Python program which queries the Pokemon API and then prints its base statistics (Attack, Defense, HP, Sp. Atk, Sp. Def, Speed)
in plain text:
```text
Charmeleon
Attack: 64
Defense: 58
HP: 58
Sp. Atk: 80
Sp. Def: 65
Speed: 80
```