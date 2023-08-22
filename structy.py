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
