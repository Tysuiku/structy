def greet(s):
    return f"hey {s}"

def max_value(nums):
  res = nums[0]
  for num in nums:
    if num > res:
      res = num
  return res

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def uncompress(s):
  numbers = "0123456789"
  result = ""
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j+=1
    else: 
      num = int(s[i:j])
      result += s[j] * num
      j += 1
      i = j
    
  return result