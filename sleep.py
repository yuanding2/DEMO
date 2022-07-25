#!python3
import time
i=0
while True:
    print(str(i)+time.asctime(),end="\r")
    i+=1
    time.sleep(1)

