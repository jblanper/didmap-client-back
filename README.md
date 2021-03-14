# didmap-client-back

Unofficial Python API client for https://mapasinteractivos.didactalia.net

The *Swagger* documentation of the API can be access in the following link: https://didmap-api.herokuapp.com/

## Intallation

In the root directory type the following command:
```
$ python -m setup.py install
```

Start a virtual environment (as it is explain in the [Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/))
```
$ pip install virtualenv
$ cd project_folder
$ virtualenv venv
$ source venv/Scripts/activate
```

Then, install the dependencies
```
& pip install -r requirements.txt
```

Use the following command to stop the virtual environment:
```
$ deactivate
```

## Local developement

You can start the *uvicorn* server with the following command:
```
$ start-dev
```
