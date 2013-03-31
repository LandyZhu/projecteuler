max = 500

for x in range(max):
    for y in range(max):
        if x**2 + y**2 == (1000-x-y)**2:
            print 'x = %d, y = %d, z = %d' % (x, y, 1000-x-y)
            print 'the product of abc is %ld' % (x*y*(1000-x-y))