# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
    words = get_dictionary()
    for w1 in words:
      for w2 in words:
        if (w1+w2) == password:
          print("exist")
          return True
    return False


def triple_words(password):
  words = get_dictionary()
  guesses = 0
  with open('dictionary.txt') as f:
    for w1 in words:
      guesses+=1
      if w1 in password:
        for w2 in words:
          guesses+=1
          if w2 in password:
            for w3 in words:
              guesses+=1
              if (w1+w2+w3) == password:
                return True, guesses
  return False, guesses
