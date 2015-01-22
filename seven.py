#!/home/hacker/sandboxpy3/bin/python
from math import floor
known_prime_nos = [2]

def check_prime(n):
    limit = floor(n**0.5)
    for i in known_prime_nos:
        if n%i==0:
            return False
        if i > limit:
            break
    return True

j = 3
count = 1
while True:
    if check_prime(j):
        if count < 70:
            known_prime_nos.append(j)
        count += 1
        if count == 10001:
            desired_prime_no = j
            break
    j +=1

print(desired_prime_no)

