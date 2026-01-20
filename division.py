def divide(numerator, denominator):

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Inputs must be numbers."

