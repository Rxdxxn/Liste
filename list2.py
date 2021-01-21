with open('input.txt','r') as f:
    a=list(eval(f.readline()))
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