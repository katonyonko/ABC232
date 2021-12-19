import io
import sys

_INPUT = """\
6
3 4
.#..
..#.
..##
1 1
.
5 5
.....
.....
.....
.....
.....
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  C=[input() for _ in range(H)]
  r=[[1]*W for _ in range(H)]
  ans=0
  for i in range(H):
    for j in range(W):
      if i==j==0:
        r[i][j]=0
      if i>0 and r[i-1][j]==0 and C[i][j]=='.':
        r[i][j]=0
      if j>0 and r[i][j-1]==0 and C[i][j]=='.':
        r[i][j]=0
      if r[i][j]==0:
        ans=max(ans,i+j+1)
  print(ans)