import time

time1 = time.clock()

prime_list = [2,3,5,7,11,13,17,19,23]

def is_prime(x):
    for i in prime_list:
        if x % i == 0:
            return False
    return True

x = prime_list[-1] + 1
while len(prime_list) != 10001:
    if is_prime(x):
        prime_list.append(x)
        x = prime_list[-1] + 2 #ignore all even numbers.
        continue
    else:
        x += 1

print prime_list[-1]
time2 = time.clock()

print (time2 - time1)