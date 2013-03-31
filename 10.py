prime_list = [2,3,5,7,11,13,17,19,23]

def is_prime(x):
    for i in prime_list:
        if x % i == 0:
            return False
    return True

x = 25
while x < 2000000:
    if is_prime(x):
        prime_list.append(x)
        print "%d" % (x)
    x += 2
        
print sum(prime_list)