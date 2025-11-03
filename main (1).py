# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

password = input("Enter password:")

print("Analyzing a triple-word password ...")
time_start = time.time()

# attempt to find password
found, guesses = pwa.triple_words(password)
time_end = time.time()

# report results
if (found):
  print(password, "founded", guesses, "guesses")
else: 
  print(password, "NOT found")
print("Time:", format((time_end-time_start), ".8f"))