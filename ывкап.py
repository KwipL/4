# s = 'a,b,c'
# print(s)
# for a in range(0,2):
#     for b in range(0, 2):
#         for c in range(0, 2):
#             if (a and not(c)) or (not(b) and not(c)):
#                 print(a,b,c)
#Ответ:cba
#
# for i in range(96,1000):
#     s = bin(i)[2:]
#     s = str(s)
#     for n in range(3):
#         if s.count('1') == s.count('0'):
#             s += s[-1]
#         elif s.count('1') > s.count('0'):
#             s += '0'
#         else:
#             s += '1'
#     r = int(s,2)
#     if r%4 ==0:
#         print(i)
#         break
#Ответ:103

# s = 146*'5'
# while '333' in s or '555' in s:
#     if '555' in  s:
#         s = s.replace('555','3')
#     else:
#         s = s.replace('333','5')
# print(s)
#Ответ:55

# p1,p2,q1,q2 = 20,30,5,53
# P = [i/10 for i in range(p1*10,p2*10)]
# Q= [i/10 for i in range(q1*10,q2*10)]
# def f(x,A):
#     return ((x in A) and ((x in Q) <= (x in P)))
# A =set()
# for x in [i/10 for i in range(190,500)]:
#     if not f(x,A):
#         A.add(x)
# print(max(A))
def F(n):
    if n == 16: return 1
    elif n >16: return 0
    else: return F(n+1) + F(n*2)
print(F(3))
