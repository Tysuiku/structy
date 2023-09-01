def greet(s):
    return f"hey {s}"

#--------------------------------------------------------------

def max_value(nums):
  res = nums[0]
  for num in nums:
    if num > res:
      res = num
  return res

# Time: O(n)
# Space: O(1)

#--------------------------------------------------------------

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

#better way

from math import sqrt, floor

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, floor(sqrt(n)) + 1): 
    #only need to test up to sqrt to determine if prime
    #plus 1 is to account for exclusive
    if n % i == 0:
      return False
    
  return True

# Time: O(square_root(n))
# Space: O(1)

#--------------------------------------------------------------

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
      #line 36 increases time complexity in python strings are immutable 
      #meaning that adding to a string will need to copy over the string then add the new string 
      # o(n^2m)
      j += 1
      i = j
    
  return result

#better way

def uncompress(s):
  numbers = "0123456789"
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j+=1
    else: 
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
    
  return "".join(result)

# Time: O(n*m)
# Space: O(n*m)

#--------------------------------------------------------------
def compress(s):
  s += "!"
  result = ""
  i = 0
  j = 0
  
  while j  < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      num = j - i
      
      if num == 1: 
        result += s[i] #increases time complexity in python strings are immutable
      else:
        result += str(num) + s[i] #increases time complexity in python strings are immutable
      
      i = j
      
  return result 
  #O(n^2) runtime

def compress(s):
  s += "!"
  result = []
  i = 0
  j = 0
  
  while j  < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      
      if num == 1: 
        result.append(s[i])
      else:
        result.append(str(num))
        result.append(s[i])
      
      i = j
      
  return "".join(result)

#--------------------------------------------------------------

def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)
  
def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    
    count[char] += 1
    
  return count

# this solution uses a helper function to solve for anagrams
# function is linear so O(n + m)

from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

#python specific built in modulo allows us to convert a string into a dictionary form 

#--------------------------------------------------------------
#my solution
def most_frequent_char(s):
  count = char_count(s)
  freq = 0
  result = ""
  
  for char in s:
    if count[char] > freq:
      freq = count[char]
      result = char
      
  return result

def char_count(str):
  count = {}
  for char in str:
    if char not in count: 
      count[char] = 0
      
    count[char] += 1 
    
  return count

#O(n) solution

def most_frequent_char(s):
  count = {}
  for char in s:
    if char not in count:
      count[char] = 0    
    count[char] += 1
    
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best

#--------------------------------------------------------------
