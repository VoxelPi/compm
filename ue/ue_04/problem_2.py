import random
import time
import numpy as np

def tic():
    global start
    start = time.time()

def toc():
    if 'start' in globals():
        print("time: {}".format(str(time.time() - start)))
    else:
        print("toc(): start time not set")

def my_max(list):
    max_val = -1
    for i in list:
        if i > max_val:
            max_val = i
    return max_val

# Generate random numbers with random.sample.
random_numbers = random.sample(range(100000000), 10000000)
random_numbers_array = np.array(random_numbers)

# Generate random numbers with numpy. (faster)
# random_numbers_array = np.random.random(10000000) * 100000000
# random_numbers = list(random_numbers_array)

# Compute the maximum element using own implementation.
tic()
print(my_max(random_numbers))
toc()

# Compute the maximum element using build-in implementation.
tic()
print(max(random_numbers))
toc()

# Compute the maximum element using numpy implementation.
tic()
print(np.max(random_numbers_array))
toc()