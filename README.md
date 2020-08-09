# Django App

> A Django Web App made using OpenWeatherMapAPI and GITHUB API to fetch data and display it on the basis of the user's search.<br />

> Weather Web Part allows the user to search weathers of different countries and add them to the favourites which can later be viewed with updated data.It also features a part where you can search any city in the world to check their weather without saving them.We can also view the top three most searched cities with their weather information.<br />

> Github Web Part allows you to search github users based on their usernames and it fetches the image,name,repositories,followers and following and other relevant information.<br />

> This Web App is mainly made to use and practice using APIs with Django.<br />

# Tasks

> Create a python file with one function, that takes 2 numbers as input. These numbers represent a
range. The expected output is to check if the numbers contain 2 adjacent 1s in their binary
equivalent and return a dictionary with each number as a key and the value as either True or False.
For example:<br />
Input: 2, 7<br />
Output: { 2: False, 3: True, 4: False, 5: False, 6: True }<br />

> Create a view that will import the above python file and call that function from the views. Supply
input to this view function using parameters provided to the function via dynamic URL. Return the
response in the form of a dictionary as mentioned in Task 1.
Note: You should implement the above function using Django views and give the output using
HTTPResponse (or JSONResponse).

> Create a view that will get input from a form, and query an API using the form values. You can use
any API for this purpose, some common ones include Github, SpaceX and Twitter. Use the
requests package of python for this purpose, to send a GET/POST request to the API and get JSON
data. You can use the Django Forms for this purpose, but it will fetch you extra points if you can
manage to handle a custom form built completely in the HTML template using the form tag and the
Django {% url %} template tag.
Note: Use requests module for Python 3 for API requests.

> You should create a database model and modify the view created in Task 3 to store all the
successful requests made to the API and add an additional count field with default value 0. Create
another view that will get input from a form for a specific field, query the database based on that
specific field value and return the response on the same page. Every time the database is queried,
update the count value for the objects matching that query by 1 and return the objects.
Create a different page that will retrieve the top 3 values from the database based on their count
values and display them using Django templates.

# Overview Of The Website

<p align="center">Task 1,2</p>
<p align="center">
 <img src="./weather_app/images/0.png">
</p>

<p align="center">Weather-Main</p>
<p align="center">
 <img src="./weather_app/images/1.png">
</p>

<p align="center">Weather-Search Any</p>
<p align="center">
 <img src="./weather_app/images/2.png">
</p>

<p align="center">Weather-Most Searched</p>
<p align="center">
 <img src="./weather_app/images/3.png">
</p>

<p align="center">Github</p>
<p align="center">
 <img src="./weather_app/images/4.png">
 <img src="./weather_app/images/5.png">
</p>

> Clone the repository.<br>
> Install django and other required dependencies.Also make sure to have installed Python and Pip.<br>
> Run npm start in the command line to run the website on local host.

## App Info

### Author [Yash Jhaveri](https://www.linkedin.com/in/yash-jhaveri-3b0882192/)
