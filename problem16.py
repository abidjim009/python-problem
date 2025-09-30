#how to read a number n and compute n+nn+nnn in python

a = int(input("Enter a number: "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )

print (n1+n2+n3) 