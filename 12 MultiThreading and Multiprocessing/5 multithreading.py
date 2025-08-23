###When to use multithreading:-
#### I\O bound tasks: tasks that spend more time waiting for I\O operations. (file operations, network requests)
#### Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently.


import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'number: {i}')

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'letter: {letter}')

# Create 2 separate threads to see their concurrent working.
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# Start the thread:-
t1.start()
t2.start()

# waits for the thread to complete.
t1.join()
t2.join()


finished_time = time.time() - t
print(finished_time)