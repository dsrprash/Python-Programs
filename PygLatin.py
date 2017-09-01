pyg = 'ay' #suffix to convert 

original = raw_input('Enter a word:') #taking input from user

if len(original) > 0 and original.isalpha():
  #checking input is valid or not
  word = original.lower() #making all characters into lowercase
  first = word[0] #fetching first char of word
  new_word = word + first + pyg #concatening into latin
  new_word = new_word[1:len(new_word)] #business logic
  print new_word
else:
  print 'empty'