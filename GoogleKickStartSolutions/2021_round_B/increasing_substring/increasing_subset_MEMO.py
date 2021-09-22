def maxSubstring(i): 
  if i == 0:
    memo[i] = 1
    return memo[0]
  
  else:
    if c[i-1] < c[i]:
      if memo[i-1] < 0:
        memo[i] = maxSubstring(i-1) + 1
        return memo[i]
      else:
        memo[i] = memo[i-1] + 1
        return memo[i]
    else:
      memo[i] = 1
      return memo[i]


  
    
if __name__=='__main__':
  #testcases = T
  testcases = int(input())

  for caseNo in range(1, testcases + 1):

    teststringlen = int(input())
    teststring = input()
    c = list(teststring)
    memo = []
    memo = [-999 for i in range(teststringlen)]


    print(f"Case #{caseNo}:", end=" ")
    for i in range(teststringlen):
      print(f'{maxSubstring(i)}', end=' ')
    #\n
    print()