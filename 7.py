prime_list = [2,3,5,7,11,13,17,19,23]

def is_prime(x):
    for i in prime_list:
        if x % i == 0:
            print str(x) + ' is not a prime.'
            return False
    print str(x) + ' is a prime'
    return True

x = prime_list[-1] + 1
while len(prime_list) != 10001:
    if is_prime(x):
        prime_list.append(x)
        print 'Find a new prime ' + str(x)
        print 'The prime number is ' + str(len(prime_list))
        x = prime_list[-1] + 2 #ignore all even numbers.
        continue
    else:
        x += 1
print prime_list
print prime_list[-1]

    