from threading import Thread
from threading import Timer
import time

class GameTimer:
    is_timer_on = False

    def __init__(self, func, timeout) -> None:
        self.func = func
        self.timeout = timeout

    def start(self):
        is_timer_on = True

        start_time = 0
        end_time = 0
        total_time_on = 0

        while is_timer_on:
            start_time = time.time()
            end_time = time.time()

            total_time_on += end_time - start_time
            print(total_time_on)
            
            if total_time_on < self.timeout:
                self.func
                total_time_on = 0

    def stop():
        is_timer_on = False

#def test():
#    print('Hello')
#
#def start_timer():
#    for x in range(0,2):
#        t = Timer(2, test)
#        t.start()

#threads = []
#t = Thread(target=start_timer)
#threads.append(t)

# Start each thread
#for t in threads:
#    t.start()

# Wait for all threads to finish
#for t in threads:
#    t.join()
