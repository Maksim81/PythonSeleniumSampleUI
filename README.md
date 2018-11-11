# PythonSeleniumSampleUI
Sample of UI tests (Python / Selenium)
Preparing environment

Current solution is based on Ubuntu OS (www.ubuntu.com), but actually many others linux distributives could be used. It is recommended (but not obligated) to have a built-in Python interpreter.

Main steps:

1. Download and install Linux OS (www.ubuntu.com)
2. Open the terminal
3. Verify that OS have built-in Python (just type python or python3). In case of installed python you will see the output with python version.

Configuring the python and related components setup

Main steps:

1. Go to the terminal
2. Install the pip for python: sudo apt-get install python-pip
3. Install the selenium extension: sudo pip install selenium
4. Create the directory for UI tests: mkdir uitest
5. git clone https://github.com/Maksim81/PythonSeleniumSampleUI.git

Running the UI tests

1. Before running the tests verify that path is set correctly for geckodriver. Change the path in the line self.driver = webdriver.Firefox(executable_path='/home/osboxes/uitest/geckodriver') to the correct one.
2. Execute the tests by command: python test3.py. Browser starts automatically and after completion you should see test execution results in the terminal
