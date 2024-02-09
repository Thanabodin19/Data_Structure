def Fibonacci(n):
    x = 0
    y = 1

    if n < 0:
        print("Please enter a positive integer")
    else:
        for i in range(n):
            z = x+y
            x = y
            y = z
            print(x, end=' ')
    
if __name__ == "__main__":    
    num = int(input("How many terms? "))
    Fibonacci(num)
