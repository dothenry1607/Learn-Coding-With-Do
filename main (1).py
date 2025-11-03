# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

password = input("Enter password:")

print("Analyzing password ...")
time_start = time.time()

found, guesses = pwa.password_word_break(password)
time_end = time.time()

if (found):
  print(password, "founded in", guesses, "guesses")
else: 
  print(password, "not found in ", guesses, "guesses")
print("Time:", format((time_end-time_start), ".8f"))