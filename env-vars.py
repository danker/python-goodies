import os

token = os.environ.get('SECRET_TOKEN')

print("The secret token is: {}".format(token))