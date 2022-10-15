N=int(input())
a = [int(s) for s in input(). split()]
P = int(input())
a.inster(0, a.pop(P-1))
print(" ".join([str(x) for x in a]))