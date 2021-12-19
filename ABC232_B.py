import io
import sys

_INPUT = """\
6
abc
ijk
z
a
ppq
qqp
atcoder
atcoder
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=input()
  ans='Yes'
  diff=(ord(S[0])-ord(T[0]))%26
  for i in range(len(S)):
    if diff!=(ord(S[i])-ord(T[i]))%26:
      ans='No'
  print(ans)