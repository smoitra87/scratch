from fabric.api import env

def hello():
	print("Hello World!")
	print(env.local_user)
	env.local_user="me"
	print(env.local_user)
