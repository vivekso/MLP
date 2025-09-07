import multiprocessing as mp
import time

def squareNumber(numbers):
    for number in numbers:
        time.sleep(2)
        print(f"Number is {number} and square is {number**2}")

def cubeNumber(numbers):
    for number in numbers:
        time.sleep(1.5)
        print (f"Number is {number} and Cube is {number**3}")

numbers = list(range(1,6))

process1 = mp.Process(target=squareNumber, args=(numbers,))
process2 = mp.Process(target=cubeNumber, args=(numbers,))
process1.start()
process2.start()
process1.join()
process2.join()

start_time = time.time()
# squareNumber(numbers)
# cubeNumber(numbers)
print(time.time() - start_time)