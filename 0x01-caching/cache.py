

import time

cache = {}

def cached(func):
    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)

        cache[args] = result

        return result

    return wrapper

@cached
def long_running_function(arg1, arg2):
    print("Running long running function...")

    # Simulate a long running process by sleeping for 5 seconds. 
    time.sleep(5)

    # Calculate the result. 
    result = arg1 + arg2

    return result 
    
# Call the function with arguments 1 and 2. 
result1 = long_running_function(1, 2)  # This will take 5 seconds to run. 
print("Result 1:", result1)   # Result 1: 3 
# Call the function again with arguments 1 and 2.  This time it should be much faster since it is cached. 
result2 = long_running_function(1, 2)   # This will be almost instantaneous since it is cached. 
print("Result 2:", result2)   # Result 2: 3