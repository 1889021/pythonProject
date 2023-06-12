def circle(r):
    pi = 3.14
    radius = 2 * pi * r
    area = r ** 2 * pi
    print("반지름은 {} 이고 원의 둘레는 {} 원의 넓이는 {} 입니다.".format(r, radius, area))


r = float(input("반지름을 입력해주세요."))
circle(r)