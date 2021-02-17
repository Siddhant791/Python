from functools import reduce
l=[1,2,3,4,5,6,7,9,8,10]
out = reduce(lambda a,b:a+b,list(map(lambda n:n*n,list(filter(lambda n:n%2==0,l)))))
print(out)
l.sort(reverse = True)
print(l)