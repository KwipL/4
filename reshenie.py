# f = 3*16**8 - 4**5 + 3
# s = ''
# while f != 0:
#     s+= str(f%4)
#     f = f//4
# print(s.count('3'))
# def F(n):
#     if n>= 10000: return n
#     if n < 10000 and n%2==0: return F(n+1) + n**2 -3*(n-1)
#     if n < 10000 and n%2!=0: return F(n+2) +4*n +1
# print(F(9950)-F(9999))
# def f(x, y):
#  if x > y: return 0
#  if x == y: return 1
#  return f(x + 1, y) + f(x + 2, y)
# def f1(x, y):
#  if x > y or x == 17 or x == 23: return 0
#  if x == y: return 1
#  return f1(x + 1, y) + f1(x + 2, y)
#
# print(f(11, 29) - f1(11, 29))
# p1,p2,q1,q2,r1,r2 =5,110,15,42,25,70
# P = [i/10 for i in range(p1*10,p2*10)]
# Q = [i/10 for i in range(q1*10,q2*10)]
# R = [i/10 for i in range (r1*10,r2*10)]
# def f(x,A):
#      return ((x in P) <= (x in Q)) or ((not(x) in A) <= (not(x in R)))
# A = set()
# for x in [i/10 for  i in range(5,1100)]:
#      if not f(x, A):
#          A.add(x)
# print(sorted(A))
f = open('17.txt')
a =[int(i) for i in f]
k = 0
m = -999999990
for i in range (len(a)-1):
    if a[i] % 117 == m or a[i + 1] % 117 == mi:
        k = k + 1
        m = max(m, a[i] + a[i + 1])
print(k, m)