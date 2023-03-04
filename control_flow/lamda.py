l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]

def change_words(words, func):
    for word in words:
        print(func(word))

def upper(word):
    return word.capitalize()

change_words(l, upper)

print("-----")

# lambda
upper = lambda word: word.capitalize()
lower = lambda word: word.lower()

print('upper ==========')
change_words(l, upper)
print('lower ==========')
change_words(l, lower)

print("-----")

# より短く書く
change_words(l, lambda word: word.capitalize())
