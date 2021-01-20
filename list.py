a=[-3,-8,-6,-1,0,1,9,3,4,6,7]
print("lista 1:",a)
b=sorted(a)
print("lista 2:",b)
c=sorted(a,reverse=True)
print("lista 3:", c)
print("numarul de elemente:",len(a))
print("maximul:",max(a))
print("minimul:",min(a))
a.extend([111])
print("lista 4:",a)
a[1]=222
print("lista 5",a)

