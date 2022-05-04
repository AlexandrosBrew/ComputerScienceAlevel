import os
import time

mainDirectory = os.getcwd()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


while True:
	dirlist = os.listdir()
	removedFiles = [".git", ".upm", "poetry.lock",
									"pyproject.toml", "README.md", "main.py", ".DS_Store", ".replit", ".txt"]
	for a in removedFiles:
			try:
					dirlist.remove(a)
			except:
					pass
	for i in range(len(dirlist)):
			print("%s: %s" % (i+1, dirlist[i]))
	print("-1: Back to start")

	userInput = int(input("Selection: "))
	clearConsole()
	try:
		if userInput == -1:
			os.chdir(mainDirectory)
		elif dirlist[userInput-1].endswith(".py"):
				os.system('python "%s"' % dirlist[userInput-1])
				print("="*50)
				print()
		else:
				os.chdir(dirlist[userInput-1])
	except:
		print("Invalid selection.\nTry again.")
		time.sleep(1.5)
		clearConsole()
	print()