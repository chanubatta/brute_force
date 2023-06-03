import os,platform

os.system('git pull')

 if __name__ == "__main__":

	try:

		__import__("run").Login()

	except Exception as e:

		exit(str(e))

 
