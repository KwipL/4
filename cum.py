# import functools
#
# def cache(func):
#     """Кэш предыдущих вызовов функций"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper.cache:
#             wrapper.cache[cache_key] = func(*args, **kwargs)
#         return wrapper.cache[cache_key]
#     wrapper.cache = dict()
#     return wrapper
#
# @cache
# def f(n):
#     if n <= 3:
#         return n + 3
#     elif f(n-1) % 2 == 0:
#         return f(n-2) + n
#     elif f(n-1) % 2 != 0:
#         return f(n-2) + 2*n
#
# k = 0
# for n in range(40, 50+1):
#     k += f(n)
#
# print(k) # 8508
# n =143
# n = bin(n-1)
# n = n[2:len(n):1]
# n1 = n.replace('1','a')
# n2 = n1.replace('0','1')
# n = n2.replace('a','0')
# n =int(n,2)
# print(n)
# s = '1'*2019 + '2'*2019
# while '222' in s:
#     if '222' in s:
#         s = s.replace('222','1')
#         s = s.replace('111','2')
# print(s)
#f = 32**60 + 4**180 -128
#s =''
#while f > 0:
    #s += str(f%8)
    #f = f//8
#print(s.count('7'))
# def F(n):
#     if n<=3: return n
#     if n >3:
#         if n%2==0: return n+3+F(n-1)
#         if n%2!=0: return n*n+F(n-2)
# k = 0
# for i in range(1,1001):
#     if F(i)%7==0:
#         k+=1
#  print(k)
# p1,p2,q1,q2 =20,80,35,57
# P = [i/10 for i in range(p1*10,p2*10)]
# Q = [i/10 for i in range(q1*10,q2*10)]
# def f(x,A):
#     return (x in A) and ((x in Q) <= (x in P))
# A = set()
# for x in [i/10 for  i in range(0,800)]:
#     if not f(x, A):
#         A.add(x)
# print(sorted(A))
def F(x,y,p):
    if x + y >= 90 and p ==4: return True
    if x + y < 90 and p == 4: return False
    if x + y >= 90: return False

    if p%2==0:
        return F(x+1,y,p+1) and F(x*3,y,p+1) and F(x,y+1,p+1) and F(x,y*3,p+1)
    else:
        return F(x + 1, y, p + 1) or F(x * 3, y, p + 1) or F(x, y + 1, p + 1) or F(x, y * 3, p + 1)
for s in range(1,81):
    if F(s, 9, 1):
        print(s)