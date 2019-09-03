# Flask

Playground for flask applications

## RestPlusAPI

A simple REST API made with flask-restplus.

The best way to use this project is by using virtual environments.

```pip install virtualenv```
```
cd RestPlustAPI
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Done using your virtual environment?
```
deactivate
```

If you have problems that the python interpreter cannot find the RestPlusAPI module, be sure to include the top flask folder into the PYTHONPATH and not the RestPlusAPI folder itself.
So, something like

```
export PYTHONPATH=${PYTHONPATH}:/yourpath/flask/
```

and **NOT**

```
export PYTHONPATH=${PYTHONPATH}:/yourpath/flask/RestPlusAPI
```

If you are using an IDE like IntelliJ IDEA, you can configure this in the project configuration (top right dropdown, next to the run button) and check

* Add content roots to PYTHONPATH
* Add source roots to PYTHONPATH

and change the working directory to the flask folder.

Also be sure that you are using the python interpreter of the virtual environment and not your globally installed one.

TODO

- [ ] Use dot-env (.env file) instead of settings.py


## My-sample-project

If you don't want to install mysql on your machine, just use docker instead.

```
docker run -p 3306:3306 --name my-mysql-container -e MYSQL_ROOT_PASSWORD=mysecret -d mysql:latest
```

Or create a docker-compose file

```
mysql:
  build: docker-build-contexts/mysql
  ports:
    - 3306
  environment:
    - MYSQL_DATABASE=mydatabase
    - MYSQL_ROOT_PASSWORD=mypassword
```

Getting the ip of the docker container:

```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
```

Connecting to running container:

```
docker exec -it <container name> /bin/bash
```

Mysql commands inside the container:

```
mysql -u -p 
<type in your password>
mysql> CREATE DATABASE my_database;
mysql> USE my_database;
mysql> CREATE TABLE user(user_name varchar(30));
mysql> INSERT INTO user(user_name) VALUES('John');
mysql> INSERT INTO user(user_name) VALUES('Peter');
mysql> SELECT * from user;
mysql> UPDATE user SET user_name='Matthew' WHERE user_name='Peter';
mysql> DELETE FROM user WHERE user_name='John';
mysql> SELECT * FROM user;
```

This project uses flask-sqlalchemy instead of flask-mysqldb.
It is also using python-dotenv instead of pyyaml. 