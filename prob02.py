num=int(input("숫자를 입력하시오"))
sum=0

for i in range(1, num+1):
    if not i%2:
       sum=sum+i
print(f'the sum is {sum}')