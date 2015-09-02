def sqrt_approx():
    x = int(input("Give a positive number. "))
    y = 1
    while round((y**2 - x), 3) != 0:
        y = (y+x/y)/2.0
        
    print("The square root of {} is {}".format(x,y))
sqrt_approx()

