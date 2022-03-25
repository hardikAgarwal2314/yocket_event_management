### yocket_event_management

## Setup

The first thing to do is to clone the repository:

```sh
$  https://github.com/hardikAgarwal2314/yocket_event_management.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

Now create a super user by command
```
python manage.py createsuperuser. Enter your desired username and press enter.
```

And navigate to `http://127.0.0.1:8000/admin/login/`.
and use of username and password to login

the Api end Point is 
`http://127.0.0.1:8000/api/events/`

if you hit a get request on this URL you will get all the events list and if
you hit post api with required body in json foramt it will create the new event in the DB

Sample Body :
```
{
    "event_name": "Event 34",
    "starting_time": "01/04/20 01:55:19",
    "duration": "60"
}
```
