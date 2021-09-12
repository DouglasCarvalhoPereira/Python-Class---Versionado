#DUAS MANEIRAS DE CRIAR UM PIG LATIN

#PRIMEIRA
def pig_latin(text):
  # Separate the text into words
  words = text.split()
  new_string = []
  for word in words:
    word = word[1:] + word[0] + 'ay'
    # Create the pig latin word and add it to the list
    new_string.append(word)
    # Turn the list back into a phrase
  return ' '.join(new_string)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

#SEGUNDA
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  new_string = []

  for word in words:
    # Create the pig latin word and add it to the list
      word = list(word)
      word.append(word[0])
      word.remove(word[0])
      word.append('ay')
      new_word = ''.join(word)
      new_string.append(new_word)
      
      result = ' '.join(new_string)
      
     # Turn the list back into a phrase
  return result
  
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
