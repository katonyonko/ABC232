import io
import sys

_INPUT = """\
6
4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4
5 6
1 2
1 3
1 4
3 4
3 5
4 5
1 2
1 3
1 4
1 5
3 5
4 5
8 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import itertools
  N,M=map(int,input().split())
  T=[]
  for i in range(M):
    A,B=map(int,input().split())
    A-=1
    B-=1
    T.append((A,B))
  S=set()
  for i in range(M):
    C,D=map(int,input().split())
    C-=1
    D-=1
    S.add((C,D))
  ans='No'
  for x in itertools.permutations(list(range(N)),N):
    tmp=set()
    for i in range(M):
      p,q=T[i]
      a,b=x[p],x[q]
      if a>b:
        a,b=b,a
      tmp.add((a,b))
    if S==tmp:
      ans='Yes'
  print(ans)