import sys,math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

t = int(sys.stdin.readline())
for i in range(t) : 
	n,k = map(int,sys.stdin.readline().rstrip().split())
	sys.stdout.write(str(nCr(n-1,k-1))+"\n")

