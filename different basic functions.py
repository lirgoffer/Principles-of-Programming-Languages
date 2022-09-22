#Autor:Lir Goffer, ID:209103274

#1
def isPrime(x):
  """
  check if number is prime
  :param x: value to check
  :return: true for prime, false for not
  """
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

def factorSum(n):
  """
  calculates the sum of the prime factors of a number
  :param n: num to calculate its prime factors
  :return: sum of prime factors
  """
  res = 0
  for i in range(2, n):
    if n % i == 0 and isPrime(i):
      res += i
  return res


#2
def onlyPositive(f):
  """
function that receives a function and return new function
  :param f: function to define
  :return: res function
  """
  def res(x):
    """
   function that return a function depending on the value of parameter
    :param x: value to check if positive
    :return: function with positive parameter
    """
    if x >= 0:
      return f(x)
    else:
      return (f(-x))
  return res


#3
def interceptPoint(p1, p2):
  """
  Checks if lines cuts and returns the cut points
  :param p1:tuple of m,n of the first line (y=mx+n)
  :param p2:tuple of m,n of the second line (y=mx+n)
  :return: none or tuple of the cut points
  """
  m1, n1 = p1
  m2, n2 = p2
  if m1 == m2:
    return None
  x = (n2 - n1) / (m1 - m2)
  y = m1 * x + n1
  return (x, y)


#4
def printNumbersInc(start, end, num):
  """
  Recursive function that prints all numbers in ascending range except num
  :param start: first value in range
  :param end: last value in range
  :param num: The value that will not be printed
  :return: end the recursive func
  """
  if start == end + 1:
    return
  if start != num:
    print(start)
  printNumbersInc(start + 1, end, num)

def printNumbersDec(start, end, num):
  """
  Recursive function that prints all numbers in descending range except num
  :param start: first value in range
  :param end: last value in range
  :param num: The value that will not be printed
  :return: end the recursive func
  """
  if start == end - 1:
    return
  if start != num:
    print(start)
  printNumbersDec(start - 1, end, num)

def printNumbers(start, end, num):
  """
  Recursive function that prints all numbers in range except num
  :param start: first value in range
  :param end: last value in range
  :param num: The value that will not be printed
  :return: end the recursive func
  """
  if start <= end:
    printNumbersInc(start, end, num)
  else:
    printNumbersDec(start, end, num)


#5
def arrProduct(arr1, arr2):
  """
  create a chain of sub-arrays,each value from the first array appears as the number of times of the corresponding number in the second array
  :param arr1: first array-the values
  :param arr2: second array-the times
  :return: new array
  """
  res = []
  for i in range(len(arr1)):
    res += [arr1[i]] * arr2[i]
  return res


#6
def analyze(s):
  """
  Counts the number of rainy months on the list.
  :param s: list of The amount of rain per month
  :return: number of rainy month
  """
  counter = 0
  lst = s.split(",")
  for x in lst:
    if float(x) >= 75:
      counter += 1
  return counter