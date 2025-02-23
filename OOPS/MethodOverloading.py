class MethodOverloading:

    def area(self, *args):
        if len(args) == 1 and isinstance(args[0], int):  # Square
            return args[0] * args[0]
        elif (
            len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int)
        ):  # Rectangle
            return args[0] * args[1]
        elif (
            len(args) == 2
            and isinstance(args[0], (int, float))
            and isinstance(args[1], int)
        ):  # Triangle
            return 0.5 * args[0] * args[1]
        else:
            raise ValueError("Invalid arguments")


# Creating an instance
obj = MethodOverloading()

# Calling overloaded methods
square_area = obj.area(5)
rectangle_area = obj.area(3, 6)
triangle_area = obj.area(4.5, 6)

# Printing results
print("Area of square:", square_area)
print("Area of rectangle:", rectangle_area)
print("Area of right angle triangle:", triangle_area)
