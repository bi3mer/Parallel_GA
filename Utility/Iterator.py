def float_range(start, stop, step=1.0):
    '''
    TODO: this only supports a positive direction right now.

    We have to do this start + count*step rather than a continuous sum because
    floating point errors can continue through.
    '''
    count = 0
    while True:
        temp =  start + count * step
        if temp >= stop:
            break

        yield temp
        count += 1