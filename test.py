a = 1
b = 2

class A:
  a=4

c= [{"name": 123, "type": A, "obj" : A()}]

print("123", c[0]['obj'].a)
def st(a, b, c):
    a = 3
    d = [4]
    c.extend(d)
    d = [5]
    print("c=" , c)

print("a=" , a)
print("b=" , b)
st(a, b, c )
print("a=" , a)
print("b=" , b)
print("c=" , c)

def func(a, a)