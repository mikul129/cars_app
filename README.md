# cars_app
## Description

This program is a REST_API for create, update, delete, search cars in database.<br />

## Documentation

## Files

cars_api - folder with files REST_API<br />
cars_app - folder with main aplication<br />

## Libraries

apiclient==1.0.4<br />
asgiref==3.4.1<br />
certifi==2021.5.30<br />
Django==3.2.5<br />
djangorestframework==3.12.4<br />
psycopg2==2.9.1<br />
pytz==2021.1<br />
sqlparse==0.4.1<br />
typing-extensions==3.10.0.0<br />
urllib3==1.26.6<br />

## Quick start

In folder with files write a command:<br />
```
python manage.py runserver
```
Now we should have access on address:<br />
127.0.0.1:8000/cars/<br />
There are all cars in database.<br />


## API methods
[GET] 127.0.0.1:8000/cars/ - list with all cars<br />
[GET] 127.0.0.1:8000/cars?id=3 - search cars with id=3<br />
[GET] 127.0.0.1:8000/cars?reg_number=DZA2212 - search cars with reg_number=DZA2212<br />
[POST] 127.0.0.1:8000/cars/create/ - create new car<br />
Example body:<br />
```
{
    "id": 2,
    "mark": "BMW",
    "model": "e60",
    "year": 2003,
    "fuel_type": "Pet",
    "mileage": 200000,
    "reg_number": "DZA2332"
}
```
<br />
[DELETE] 127.0.0.1:8000/cars/3 - delete car with id=3<br />
[UPDATE] 127.0.0.1:8000/cars/3 - update car with id=3<br />

## Contact

mikulski.michal2@gmail.com
