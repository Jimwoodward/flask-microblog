from flask import Flask

# __name__ is a predefined variable who's value is the module the variable is used in.
# In this case, the module name is the folder name that this file exists in. So, the value of __name__ is 'app'

app = Flask(__name__) # We create the flask object named app here

# There are two 'app' entities so far. 
# We have the app package, which is a product of the __init__.py file and the subdir 'app'
# We have the flask object named app, which is a member of the app package
from app import routes














print("File1 __name__ = %s" %__name__)
  
if __name__ == "__main__": 
    print("File1 is being run directly")
else: 
    print("File1 is being imported")