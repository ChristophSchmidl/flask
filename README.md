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