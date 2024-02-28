import time
import sys

def fib_seq(n):
    
    try:
        
        # Check for valid input
        if type(n) is not int:
            raise TypeError
        if n < 1:
            raise ValueError
        
        vals = 2          # counter value to create sequence of specified length
        last_last = 0     # stores the 2nd to last value
        yield 0           # yields 0 on first generation (0th value of sequence)
        last = 1          # stores the last value
        yield 1           # yields 1 on second generation (1st value of sequence)

        while vals < n:
            new = last + last_last        # defines new value as the sum of the last two values
            last_last = last              # move the last value to be second to last
            last = new                    # move the new value to be the next last value
            vals += 1                     # increments vals
            yield new                     # yields the new value that has been defined
    
    # Handles input errors
    except TypeError:
        print('Input Error: The length, n, must be an integer')
        
    except ValueError:
        print('Input Error: The length, n, must be a positive integer')
    
    
          
                
if __name__ == '__main__':
    
    # Test 1: Example Fibonacci Sequence 
    print('Test 1: Example Fibonacci Sequence of Length 10')
    test1 = fib_seq(10)
    test_list = []
    for num in test1:
        test_list.append(num)
    print(test_list)
    print('')
    
    # Test 2: Invalid Sequence Length (1.1)
    print('Test 2: Invalid Length - Not an Integer')
    test2 = fib_seq(1.1)
    for num in test2:
        print(num)
    print('')
    
    # Test 3: Invalid Sequence Length (-4)
    print('Test 3: Invalid Length - Not a Positive Integer')
    test3 = fib_seq(-4)
    for num in test3:
        print(num)
    print('')
    
    # Test 4: Invalid Sequence Length (one)
    print('Test 4: Invalid Length - Input is a String')
    test4 = fib_seq('one')
    for num in test4:
        print(num)
    print('')
    
    # Summation of every 3rd value
    print('Summation of every 3rd Fibonacci Number in first 100,000 values:')
    it = 2
    total = 0
    
    t_start = time.perf_counter()
    
    for num in fib_seq(100000):
        if it == 2:
            total += num
            it = 0
        else:
            it += 1
            
    t_stop = time.perf_counter()  
    
    sys.set_int_max_str_digits(0)
    print(total)
    print('Elapsed Time:',t_stop-t_start,'seconds')

