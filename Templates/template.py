import sys
'''
usage:
python3 template.py < input.in > result.out
'''

def solution():
  pass



if __name__=='__main__':
  #testcases = T
  testcases = int(input())

  for caseNo in range(1, testcases + 1):
    inputs = input()
    print(f"Case #{caseNo}: {solution(inputs)}")


