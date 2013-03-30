#Solution 1
print sum(range(101))**2 - sum([x**2 for x in range(101)])
#Solution 2
print sum([x*y for x in range(101) for y in range(101) if x != y]) 
