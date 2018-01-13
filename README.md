<a href="https://flask-testing.readthedocs.io/en/latest/">
<img src="https://media.giphy.com/media/kvjrG7mRLiWm4/giphy.gif" alt="PythonSample" />
</a>

# PythonSample

## Steps to run the project

### On MacOS

1. Clone the project
2. Open in [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) or [Sublime](https://www.sublimetext.com/3)
3. Open the terminal go inside the directory 'PythonSample'
4. Execute `python --version` to see the Python version in your Mac
5. Execute `pip --version` to see whether you have installed pip already and to know it's version
6. If pip is not installed use `sudo easy_install pip` to install it
7. Install virtualenv by using the command `sudo pip install virtualenv` (virtualenv is a tool for creating isolated Python environments)
8. Execute following command `virtualenv --no-site-packages venv`
8. Execute `source venv/bin/activate`
9. Execute `pip install flask`
10. Execute `python sql.py`
11. Execute `python app.py` (Open the browser and go to localhost:5000)
12. Execute `python tests.py -v`