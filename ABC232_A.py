import io
import sys

_INPUT = """\
6
3x7
9x9
1x1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  print(int(S[0])*int(S[2]))