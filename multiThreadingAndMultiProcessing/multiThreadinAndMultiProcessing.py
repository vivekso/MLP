import threading
import time


def squareNumber(numbers):
    for number in numbers:
        time.sleep(2)
        print(f"Number is {number} and square is {number**2}")

def cubeNumber(numbers):
    for number in numbers:
        time.sleep(2)
        print (f"Number is {number} and Cube is {number**3}")

numbers = list(range(1,6))

thread1 = threading.Thread(target=squareNumber, args=(numbers,))
thread2 = threading.Thread(target=cubeNumber, args=(numbers,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

start_time = time.time()
# squareNumber(numbers)
# cubeNumber(numbers)
print(time.time() - start_time)