import sys
import math
import random
sys.set_int_max_str_digits(1000000)
print('Bobs')
print(len(str(2**7)))
print(3.1415*2)
print(math.lcm(3,10))
print(math.pi)
print(math.sqrt(16.5))
print(random.random()) # um número aleatório entre 0 e 1
print(random.choice(['a', 'b', 'c', 'd']))
print(random.choice([1,2,3,4,'aa',10]))
theta=math.pi/3
# theta=1
x=math.sin(theta)
# c=random.choice([0,1,2,3,4,5,6,7,8,9,10])
c = random.choice(range(10))+1
x=x.__round__(c)
print("sen", (180*theta/math.pi).__round__(4), "graus com", c, "casa(s): ", x)
print("sen", theta.__round__(4),"rads com", c, "casa(s):", x)
