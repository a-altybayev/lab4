# task 1
def gen_sqr(N):
    for i in range(N+1):
        yield i**2
for i in gen_sqr(int(input())):
    print(i)

#task 2
def gen_en(N):
    for i in range(N+1):
        if i%2==0:
            yield i
        else:
            yield ','
for i in gen_en(int(input())):
    print(i, end ='')

#task 3
def gen_34(N):
    for i in range(N+1):
        if i%3==0 and i%4==0:
            yield i
for i in gen_34(int(input())):
    print(i)

#task 4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
for i in squares(int(input()), int(input())):
    print(i)

#task 5
def gen_down(N):
    for i in range(N+1):
        while N>i:
            yield N
            N -= 1
for i in gen_down(int(input())):
    print(i)