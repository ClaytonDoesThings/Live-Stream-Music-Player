import audio
import threading
from queue import Queue

# Create the queue and threader 
q = Queue()

# The threader thread pulls an worker from the queue and processes it
def threader(job, args):
    while True:
        # gets an worker from the queue
        q.get()

        # Run the example job with the avail worker in queue (thread)
        if (args != None):
            job(args)
        else:
            job()
        
        # completed with the job
        q.task_done()

t = threading.Thread(target=threader, args=(audio.loop, None))
t.daemon = True
t.start()

for worker in range(1):
    q.put(worker)

print("Thread1")
q.join()