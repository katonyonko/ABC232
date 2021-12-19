import io
import sys

_INPUT = """\
6
2 2 2
1 2 2 1
1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000
3 3 3
1 3 3 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  H,W,K=map(int,input().split())
  x1,y1,x2,y2=map(int,input().split())
  a,b,c,d=0,1,1,0
  for i in range(K-1):
    a,b,c,d=(b*(H-1)+c*(W-1))%mod,(a+b*(H-2)+d*(W-1))%mod,(a+c*(W-2)+d*(H-1))%mod,(b+c+d*(H+W-4))%mod
  if x1==x2 and y1==y2:
    print(a)
  elif x1==x2:
    print(c)
  elif y1==y2:
    print(b)
  else:
    print(d)