import signal
import time

def handler(signum,frame):
    print('Signal handler called with signal',signum)
    signal.signal(signal.SIGINT,signal.SIG_DFL)

signal.signal(signal.SIGINT,handler)

while True :
    print("Waiting....")
    time.sleep(5)