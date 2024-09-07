def get_primes(num):
  primes = []
  isPrime = False
  for numToTest in range(2, num + 1):
      if (num % numToTest == 0):
        if (not primes):
          primes.append(numToTest)
        for prime in primes:
          if (numToTest not in primes and prime != 1   and numToTest % prime == 0):
            isPrime = False
        if (isPrime == True):
          primes.append(numToTest)
        else:
          isPrime = True
  return primes;

def get_prime_factors(num):
  primes = []
  numTmp = num
  for i in get_primes(num):
    numTmp = num
    while(numTmp % i == 0):
      primes.append(i)
      numTmp = numTmp / i
  return primes    


print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
print(get_prime_factors(13))  # [13]