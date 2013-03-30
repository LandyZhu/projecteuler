#My solution is not the best. Check http://projecteuler.net/thread=4 for more better solutions.

max_3_digit_number = 999
min_3_digit_number = 100
candidates = []

# I use is_palindrome() to verify the number.
# But someone has a very simple way:
# if int(str(a*b)[::-1]) == a*b

def is_palindrome(x):
    a = list(str(x))
    b = list(str(x))
    b.reverse()
    if ''.join(a) == ''.join(b):
        return True
    else:
        return False
    
def is_two_3_digit_number_product(x):
    for i in range(min_3_digit_number, max_3_digit_number):
        if (x % i) == 0:
            if (len(str(i)) == 3) and (len(str(x/i)) == 3):
                return True
            else:
                continue
        else:
            continue
    return False
        
for i in range(min_3_digit_number*min_3_digit_number, max_3_digit_number*max_3_digit_number):
    if is_palindrome(i):
        if is_two_3_digit_number_product(i):
            candidates.append(i)
        else:
            continue
    else:
        continue
    
print max(candidates)
        
            
        
                
            
    
    