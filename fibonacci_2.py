#Implementing fibonacci sequence in python using functions using python 2.7
def fibonacci(n):
    const = [0,1]
    for i in range(1,n):
        fib = const.append(const[i] + const[i-1])
    return const
print fibonacci(10)
