# Show the performance advantage of binary search over linear search by creating a list of one million numbers and timing how long it takes the linear_
# contains() and binary_contains() functions defined in this chapter to find
# various numbers in the list.

import timeit
from datetime import timedelta
from generic_search import binary_contains, linear_contains
import numpy as np

if __name__ == '__main__':

    rdn_data = np.random.randint(100000, size=1000000)
    print(np.sort(rdn_data))
    nb = 9000


    start2 = timeit.default_timer()
    rdn_data = np.sort(rdn_data)  #Include sort time
    print(binary_contains(rdn_data,nb))
    end2 = timeit.default_timer()
    print("Binary Search: ",end2 - start2)

    start = timeit.default_timer()
    print(linear_contains(rdn_data,nb))
    end = timeit.default_timer()
    print("Linear Search: ",end - start)



