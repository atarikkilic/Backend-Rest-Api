# Address Book API

This project can be used to backend Rest API.

## Getting Started

**Step 1:** Make sure git is installed on your os. I will be using Windows for the project.


**Step 2:** Clone the project into your local machine using below command.

```git clone https://github.com/atarikkilic/Backend-Rest-Api```

### Prerequisites

**1. Docker**

Make sure you have Docker installed. Please follow the below link for official documentation from Docker to install latest version of docker on your os.

```https://docs.docker.com/get-docker/```

**2. Python**

Install Python 2.7


### Installing

**Step 1:** Change to the directory where the project was cloned in previous step.

```
cd Backend-Rest-Api
```

**Step 2:** Install the following dependencies, using pip install -r requirements.txt (or pip3 instead of pip)

Where requirements.txt is:

```
alembic==1.0.1
Click==7.0
Flask==1.0.2
Flask-Login==0.4.1
Flask-Migrate==2.3.0
Flask-SQLAlchemy==2.3.2
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
mysqlclient==1.3.13
python-dateutil==2.7.4
python-dotenv==0.9.1
python-editor==1.0.3
six==1.11.0
SQLAlchemy==1.2.12
Werkzeug==0.14.1
```

**Step 3:** Make sure Docker is up and running. You can start the docker engine from desktop icon on Windows.

**Step 4:** Run

```
docker-compose up --build
```

**Step 5:** Open up the browser and paste the below url

```
http://localhost:8000/
```

The browser should display ```Hello! I am back with db running .!``` message. The app is up and running inside a docker container using docker-compose.

**Step 6:** Verify DB is up and running and tables are created

Use any of the database clients like MySQL workbench. In my case, I am using the MySQL workbench. Make sure you have the driver installed for the MySQL db running on the client you are using.

Connect to MySQL database using the properties specified in ```docker-compose.yml``` file with host as ```localhost```.

**Running:**

**1-)Add User**

•	Users be able to add new contacts by providing their information such as name, address, phone, mobile phone and e-mail 
    with /add by postman.

**2-)Edit User**

•	Users be able to update contact in the address book with /edit by postman

**3-)Delete User**

•	Users be able to delete contact from the address book with /remove by postman

**4-)Search User**

•	Users be able to search contacts by providing any of contact’s data such as name, address, phone, e-mail with /search by postman

## Built With

* [Docker](https://docs.docker.com/) -  Deployment model
* [Flask](https://flask.palletsprojects.com/) - The web framework
* [Python](https://www.python.org/) - Programming language
* [pip](https://pypi.org/project/pip/) - Package and dependency manager
* [MySQL](https://www.mysql.com/) - Database
* [VsCode](https://code.visualstudio.com) - IDE
