#Newton's Approximation of square root
def approx_square_root():
    y = 1
    x = 0
    count = 0
    try:
        x = int(input("Give a positive number. "))

    except ValueError:
        print("That is not a positive number. Try again.")
        exit()
    if x < 0:
        print("That is not a positive number. Try again.")
        exit()
    else:
        while round((y**2 - x), 3) != 0:
            y = (y+x/y)/2.0
            if y ** 2 != x:
                count += 1
                print("{} number of iterations have occurred, the new guess is {}".format(count, y))
            print("The square root of {} is {}".format(x,round(y, 3)))
approx_square_root()
