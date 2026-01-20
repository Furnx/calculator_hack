def add(a, *b):
    if not isinstance(b, tuple):
        return sum(a, b)
    else: 
        return sum(b) + a  