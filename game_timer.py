from threading import Thread
from threading import Timer
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

def test():
    print('Hello')

def start_timer():
    for x in range(0,2):
        t = Timer(2, test)
        t.start()

# Start threads for each link
threads = []
# for link in links:
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
t = Thread(target=start_timer)
threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
