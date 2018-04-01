from ydl import ydl
import audio
import threading
from queue import Queue

ydl({
    'file_name': 'audio',
    'codec': 'wav',
    'url': 'https://www.youtube.com/watch?v=8-jkyida4zw&ab_channel=billwurtz'
})

# Create the queue and threader 
q = Queue()

# The threader thread pulls an worker from the queue and processes it
def threader(job, args):
    while True:
        # gets an worker from the queue
        q.get()

        # Run the example job with the avail worker in queue (thread)
        job(args)
        
        # completed with the job
        q.task_done()

for worker in range(1):
    q.put(worker)

t = threading.Thread(target=threader, args=(audio.play, "audio.wav"))
t.daemon = True
t.start()

print("Thread1")
q.join()