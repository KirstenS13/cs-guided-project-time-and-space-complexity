# Time complexity
"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""


def number_of_steps(num):
    # overall: 0(log n)
    # O(1) + O(log n * c) --> O(c log n + 1) --> O(log n)
    steps = 0               # constant
    while num > 0:          # how many times does the loop run? -- log n times
        if num % 2 == 0:    # code w/i the loop is constant
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps

# To classify, go line by line


"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""


def sorted_squares(A):
    # overall time complexity: O(4N + 5) --> O(N)
    N = len(A)                  # O(1)
    j = 0                       # O(1)
    while j < N and A[j] < 0:   # how many times does this loop run? - at most N times -- O(N)
        j += 1                  # O(1)
    i = j - 1                   # O(1)

    ans = []                    # O()
    while 0 <= i and j < N:     # how many times does this loop run? - at most N -- O(N)
        if A[i]**2 < A[j]**2:   # O(1)
            ans.append(A[i]**2) # appending to the end of the list is usually constant
            i -= 1              # O(1)
        else:
            ans.append(A[j]**2) # O(1)
            j += 1              # O(1)

    while i >= 0:               # how many times does this loop run? - at most N -- O(N)
        ans.append(A[i]**2)     # O(1)
        i -= 1                  # O(1)
    while j < N:                # how many times does this loop run? - at most N -- O(N)
        ans.append(A[j]**2)     # O(1)
        j += 1                  # O(1)

    return ans


"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""


def insertion_sort(arr):
    # O(N*N) --> O(N^2)
    for i in range(1, len(arr)):    # O(N)
        key = arr[i]                # O(1)

        j = i-1                     # O(1)
        while j >= 0 and key < arr[j]:  # at most N --> O(N)
            arr[j + 1] = arr[j]     # O(1)
            j -= 1                  # O(1)
        arr[j + 1] = key


# Space Complexity
"""
Use Big O notation to classify the space complexity of the function below.
"""


def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])

    return lst[n-1]


"""
Use Big O notation to classify the space complexity of the function below.
"""


def fibonacci_two(n):
    x, y, z = 0, 1, None

    if n == 0:
        return x
    if n == 1:
        return y

    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z


"""
Use Big O notation to classify the space complexity of the function below.
"""


def do_something(n):
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)

    return lst
