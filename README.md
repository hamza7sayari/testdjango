# testdjango
 

1- ensure you installed
* Postgres Db

2- Then Create a  python3 virtual env  

3- then run 
* pip install - r requirements.txt

4- create an empty db called candidates

5- Then  under testdjango directory run 
* manage.py makemigrations
* manage.py migrate

6- to test  and access API's   create a super user
with 
* manage.py createsuperuser

 you could direcly view API via swagger  , just navigate to  via postman or browser
and  login with   your super user 
 * http://127.0.0.1:8000/
