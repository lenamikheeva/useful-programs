print("Wpisz a:")
a = int(input())
print("Wpisz b:")
b = int(input())

dl = a%b
counter = 1
e = a
f = b
while (dl>0):
	
	e = f
	f = dl
	dl = e%f

	counter+=1


i = [0] * counter
u = [0] * counter
u1 = [0] * counter
v = [0] * counter
v1 = [0] * counter
a1 = [0] * counter
b1 = [0] * counter
q = [0] * counter
r = [0] * counter

i[0] = 0
u[0] = 0
v[0] = 1
u1[0] = 1
v1[0] =0
a1[0] = a
b1[0] = b
q[0] = int(a1[0]/b1[0])
r[0] = a%b

for x in range(1,counter):
	i[x] = i[x-1]+1
	u[x] = u1[x-1]-q[x-1]*u[x-1]
	u1[x] = u[x-1]
	v[x] = v1[x-1]-q[x-1]*v[x-1]
	v1[x] = v[x-1]
	a1[x] = b1[x-1]
	b1[x] = r[x-1]
	q[x] = int(a1[x]/b1[x])
	r[x] = a1[x]%b1[x]

print("i","\t","u","\t","u1","\t","v","\t","v1","\t","a","\t","b","\t","q","\t","r")
for x in range(0,len(i)):
	print(i[x],"\t",u[x],"\t",u1[x],"\t",v[x],"\t",v1[x],"\t",a1[x],"\t",b1[x],"\t",q[x],"\t",r[x])
print("v =",v[-1])
