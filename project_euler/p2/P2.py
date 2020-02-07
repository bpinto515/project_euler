# Problem 2
# Bruno Pinto

class P2:
    # Functions

    # Main
    sum, count = 0, 0
    n1, n2 = 0, 1
    while count < 4000000:
        nth = n1 + n2
        #print(nth)
        if nth % 2 == 0:
            sum += nth
        n1 = n2
        n2 = nth
        count += nth

    print(sum)
