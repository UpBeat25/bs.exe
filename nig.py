import random
import re

with open("gigga.txt", "r", encoding="utf-8") as f:
    a = f.read()

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', a)
words_array = clean_text.split()

# Generate a random string of 100 words
random_words = random.choices(words_array, k=1000)
text = " ".join(random_words)

print(text)

with open("gigga.txt", "a", encoding="utf-8") as f:
    f.write(F"{text} \n")