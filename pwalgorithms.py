def get_dictionary():
    with open('dictionary.txt') as f:
        return set(line.strip() for line in f if line.strip())

def password_word_break(password):
    words = get_dictionary()
    n = len(password)
    guesses = 0
    can_segment = [False] * (n + 1)
    can_segment[0] = True  
    for i in range(1, n + 1): 
        for j in range(0, i):
            guesses += 1
            if can_segment[j] and password[j:i] in words:
                can_segment[i] = True
                break
    return can_segment[n], guesses

