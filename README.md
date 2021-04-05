# testdjango
 

ensure you installed
* Postgres Db
Create a virtual env  

then run 
*   pip install - r requirements.txt

create an empty db called candidates

Then run under testdjango directory run 
* manage.py makemigrations
* manage.py migrate

to test API's  & UI create a super user
with 
* manage.py createsuperuser

 you could direcly view API via swagger at 
 * http://127.0.0.1:8000/
