def square(number):
    try:
        if number < 1 or number > 64:
            raise ValueError("square must be between 1 and 64")
        return 2**(number-1)
    except TypeError:
        raise ValueError ("Type must be a number or integer")

def total(grains=64):
    try:
        if grains < 1 and grains > 64:
            raise ValueError("square must be between 1 and 64")
        return (2** grains) -1
    except TypeError:
        raise ValueError ("Type must be a number or integer")