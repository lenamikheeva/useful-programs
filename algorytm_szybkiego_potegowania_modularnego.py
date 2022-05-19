def into_binary(t):
	odp = []
	while (t >= 1):
		odp.append(t%2)
		t = int(t/2)

	return odp

# 2^25 mod 9 = 2; a=2, t=25=(11001)2, n=9
print("Dla 2^25 mod 9; a=2, t=25=(11001)2, n=9")
print("Wpisz a:")
a = int(input())
print("Wpisz n:")
n = int(input())
print("Wpisz t:")
td = int(input())

t = into_binary(td)
print("\n")
print("t=",t[::-1]," binarnie","\n")
t.append("-")

i_list = [0] * len(t)
x_list = [0] * len(t)
a_list = [0] * len(t)

i_list[0] = 0
x_list[0] = 1
a_list[0] = a

for i in range(1,len(t)):
	i_list[i] = i
	if (t[i-1] == 1):
		x_list[i] = (x_list[i-1]*a_list[i-1])%n
	else:
		x_list[i] = x_list[i-1]
	a_list[i] = (a_list[i-1]*a_list[i-1])%n

print("i","\t","x","\t","a","\t","t")
for i in range(0,len(t)):
	print(i_list[i],"\t",x_list[i],"\t",a_list[i],"\t",t[i])
print("Odpowiedz: ",x_list[-1])