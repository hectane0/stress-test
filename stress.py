import requests
import threading
import Queue
import time

URL = ''
FILE_NAME = 'result.txt'
THREADS_NUMBER = 100
REQUESTS_NUMBER = 5


def fetch_url():
	for num in range(0, REQUESTS_NUMBER):
		time = requests.get(URL).elapsed.total_seconds()
		q.put(time)

def queue_operating():
	open(FILE_NAME, 'w').close()
	time.sleep(1)
	for  num in range(0, THREADS_NUMBER*REQUESTS_NUMBER):
		item = q.get()
		print(item)
		with open(FILE_NAME, 'a') as f:
			f.write((str(item)).replace('.', ',') + "\n")


threads = []

queue_thread = threading.Thread(target=queue_operating)
queue_thread.start()

q = Queue.Queue()

for num in range(0, THREADS_NUMBER):
	threads.append(threading.Thread(target=fetch_url))

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
end = time.time()

queue_thread.join()
print("Execution time: " + str(end - start))