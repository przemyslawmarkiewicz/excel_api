# **Excel API**

## Project description
API that allows uploading an excel file and with a provided list of column names will find those columns and produce a summary (average and sum) in JSON format. API is supported with REST API Documentation tool - Swagger UI  
## Setup
First, get secret values - you have to create `.env` file (it should look like `.env.example`) and ask for secret variables \
To run project you can either use docker or just virtualenv. 

### Docker
You need to have docker installed. Go to the root directory of project and run following commands:
* ```docker build -t excel-api .``` 
* ``docker run -d -p 8001:8000  --rm excel-api`` 

Open the url:
* [localhost:8001](http://localhost:8001)
### Virtualenv 
* To install `virtualenv` run : ``pip install virtualenv``
* Go to the root directory of the project and create virtual environment: ``virtualenv venv``
* activate virtualenv:
    * on linux: `source venv/bin/activate` (deactivate with `deactivate` command)
    * on windows: `.\venv\Scripts\activate`
    
* install dependencies: `pip install -r requirements.txt`
* run application: `python manage.py runserver`
* application will run on your localhost: [localhost:8000](http://localhost:8000)