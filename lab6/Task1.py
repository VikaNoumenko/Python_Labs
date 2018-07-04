import time
from random import choice
from string import ascii_letters
import _thread
import  threading

list = []
lock = threading.Lock()

def generateString():
    lock.acquire()
    list.append(''.join(choice(ascii_letters) for i in range(5)))
    lock.release()
    time.sleep(1)

def saveList():
    while 1:
        outFile = open("6.txt", "a")
        lock.acquire()
        list.sort()
        for line in list:
            outFile.write(line)
            outFile.write('\n')
        outFile.close()
        lock.release()
        time.sleep(5)

def printList():
    while 1:
        lock.acquire()
        print(list)
        lock.release()
        time.sleep(3)

_thread.start_new_thread(saveList,())
_thread.start_new_thread(printList,())

while 1:
    generateString()
    time.sleep(1)


