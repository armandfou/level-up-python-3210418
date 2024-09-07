def is_palindrome(str):
  str = str.upper().replace(" ", "").replace("'", "").replace(",", "")
  for i in range((len(str) // 2) + 1):
    print(i)
    if (str[i] != str[len(str) - 1 -i]):
      print(str[len(str) - 1 -i])
      print(str[i])
      return False
  return True

print(is_palindrome("Go hang a salami, I'm a lasagna hog"))  # true