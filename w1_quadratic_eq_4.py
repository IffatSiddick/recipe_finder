import math

def quadratic_equation(a, b, c):
    denominator = 2 * a
    square_root = (b**2) - (4*a*c)
    if (square_root == 0):
        return (0, 0)
    # for solutions needing imaginary numbers
    elif (square_root < 0):
        square_root = -square_root
        root = "√" + str(square_root) + "i"
        solution_pos = "(-" + str(b) + "+" + root + ")/" + str(denominator)
        solution_neg = "(-" + str(b) + "-" + root + ")/" + str(denominator)
        return ("x1 = " + str(solution_pos) + " and x2 = " + str(solution_neg))
    else:
        root = math.isqrt(square_root)
        solution_pos = (-b + root)/denominator
        solution_neg = (-b - root)/denominator
        #x solutions are reversed to make them x = ans instead of (x +- ans)
        return ("x1 = " + str(-solution_pos) + " and x2 = " + str(-solution_neg))

# setting up the main part of the program
cont = "Y"
while (cont == "Y"):
    print('''Welcome to the quadratic equation solver!
          Enter any quadratic equation and the program will find the value of x.
          Remember the quadratic formula is ax^2 + bx + c.''')

    integer = False
    while (integer == False):
        try:
            a = int(input("What will be your a? It mut be a whole number and not a decimal. "))
            b = int(input("What will be your b? It mut be a whole number and not a decimal. "))
            c = int(input("What will be your c? It mut be a whole number and not a decimal. "))
            print("")
            integer = True
        except ValueError:
            print("You cannot use decimal numbers. Only whole numbers can be used.")
            print("")
            integer = False

    print(quadratic_equation(a, b, c))
    print("")

    cont = input("Do you want to play again? Enter either Y/N: ")
    print("")
    
