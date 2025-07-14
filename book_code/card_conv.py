def car_conv(decimal, radix):
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while decimal > 0:
        d += dchar[decimal % radix]
        decimal //= radix
    
    return d[::-1]

print(car_conv(10, 16))