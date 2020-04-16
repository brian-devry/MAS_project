# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

After downloading the Repo, run the application in a virtual environment. The repo probably has my Windows "venv" folder that I included so I could work on my multiple machines more easily.

You can create a new virtual environment using: 'python -m venv virtualenvironment' substituting virtualenvironment with a different virtual environment name. 'python3' can be used as the python command if your system also uses an old version (2.x) of python, check using '$python --version' command.

To activate/use your virtual environment on Unix, you use the following command:
'source virtualenvironment/bin/activate'

To activate the virtual environment in Windows:
'virtualenvironment\Scripts\activate'

The command prompt will then show your virtual environment's name in parenthesis to show you are running in the virtual environment: (venv) for example

# Before running the program, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
'(venv) $ export FLASK_APP=microblog.py'
on Windows use the set instead of export command:
'(venv) $ set FLASK_APP=microblog.py'

To set debug mode for auto-restart on file changes, etc:
'export FLASK_DEBUG=1' on Mac/Unix
on Windows 'set FLASK_DEBUG=1' once in the virtual environment

# To run the app, use the command: 'flask run'

You should see output similar to the following:
(venv) C:\Folder>flask run
 * Serving Flask app "microblog.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
[2020-04-15 20:01:59,315] INFO in __init__: Microblog startup
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
