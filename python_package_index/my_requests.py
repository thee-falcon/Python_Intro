import requests

response = requests.get("http://google.com")
print(response) # we got a response with a statu 200, which indicates succes.

# to activate the enevironment and work with module requests
# use the command: pipenv shell
# when you run this command basically, you lunch a subshell in virtual enviroment, of the environment source path.

# the compile your program using: python file_name.py


# to knowing the path of the environment use the command:
# pipenv --venv