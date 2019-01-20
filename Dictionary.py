
dic1 = {x:x*2 for x in range(5)}
print (dic1[2])

dict2 ={n:n*2 for n in range(10) if n%2 ==0}
print (dict2)


l1 = [x for x in range(5)]
print(l1)

l2 = [x for x in range(10) if x %3 ==0]
print(l2)

x = [1, 2, 3]
x.append([4, 5])
print (x[3][1])


x = [1, 2, 3]
x.extend([4, 5])
print (x[4])


dict2 ={n:n*2 for n in range(10) if n%2 ==0}
print (dict2)


dict2[10] =200
print (dict2)

for i in dict2:
	print(dict2[i])

del (dict2[0])
del (dict2[2])



dict1 ={n:n*3 for n in range(10) if n%3 ==0}
print (dict1)

del (dict1[0])



dict3 = { 'One' : dict1 ,  'Two' :	 dict2	}
print (dict3)

print(dict3['One'])


for i in dict3:
	for j in dict3[i]:
		print (dict3[i][j])
		
		
li1= [x for x in range(10) if x%2]
print (li1)

se11 = set([1,2,212,3,3,3,31,1])
print(se11)


set2= {x for x in range(4)}
print(set2)
	
	
	
	
