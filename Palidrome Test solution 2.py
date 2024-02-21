def palindrome_checker(inputString):
  if inputString.lower() == inputString[::-1].lower():
    return True
  else:
    return False

word = input("What word would you like to check to see if it is a palidrome? ")

if palindrome_checker(word):
  print ("This is a palindrome")
else: 
  print ("This is not a palindrome")