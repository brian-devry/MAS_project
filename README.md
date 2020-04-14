# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

After downloading the Repo, run the application in a virtual environment: venv for windows, macvenv for mac/unix
You can create a new virtual environment using: 'python -m venv virtualenvname' of course substituting your virtual environment name. python3 can be used as the python command if your system uses an old version (pre-3) of python, check using '$python --version'.


To activate/use your virtual environment, you use the following command:
'source venv/bin/activate'
to activate the virtual environment in Windows:
'venv\Scripts\activate'

The command prompt will then show your virtual environment's name in parenthesis to show you are running in the virtual environment: (venv) for example

Before running the program, though, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
'(venv) $ export FLASK_APP=microblog.py'
on Windows use the set instead of export command:
'(venv) $ set FLASK_APP=microblog.py'


To set debug mode for auto-restart on file changes, etc:
'export FLASK_DEBUG=1' on Mac/Unix
on Windows 'set FLASK_DEBUG=1' once in the virtual environment