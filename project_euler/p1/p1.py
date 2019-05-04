# Problem 1
# Bruno Pinto

class p1:
    
    # Functions
    def multiple(i):
        if (i%3)==0 or (i%5)==0:
            return i

    # Main
    sum = 0
    for i in range(1000):
        if multiple(i):
            sum += i

    print(sum)
    


