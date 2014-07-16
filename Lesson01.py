import time
import webbrowser

# i is counter for program, initialized to zero
i = 0

print ("This program started on " + time.ctime())
while (i < 3):
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	i += 1