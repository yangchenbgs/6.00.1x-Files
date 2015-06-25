x,y,z = 9,2,4
if x%2 != 0:
    if y%2 != 0 and z%2 != 0:
        if x > y and x > z:
            print ' x is the largest odd number'
        if y > x and y > z:
            print ' y is the largest odd number'
        if z > x and z > y :
            print ' z is the largest odd unmber'
    if y%2 == 0 and z%2 != 0:
        if x > z :
            print 'x is the largest odd number'
        if z > x :
            print 'z is the largest odd number'
    if y%2 != 0 and z%2 == 0:
        if x > y:
            print 'x is the largest odd number'
        if y > x :
            print ' y is the largest odd number'
    else:
        print ' x is the largest odd number'
elif y%2 == 0:
    if z%2 != 0:
        print' z is the largest odd number'
    if z%2 == 0:
        print' non of them are odd'
elif y%2 !=0 :
    if z%2 == 0:
        print ' y is the largest odd number'
    elif y > z:
        print 'y is the largest odd number'
    else:
        print' z is the largest odd number'