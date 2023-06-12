import random
sum=0
iter=10
for step in range(iter):
    rnum=random.randint(1,6)
    sum=sum+rnum
print(f'the average is {sum/iter}')