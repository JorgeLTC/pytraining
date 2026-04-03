import string
from collections import Counter

word_freq = Counter()
try:  # We error handle
    with open(
        "data.txt", "r", encoding="utf-8"
    ) as file:  # We handle opening up a file and we read it
        for line in file:
            cleaned_line = line.translate(
                str.maketrans("", "", string.punctuation)
            ).lower()
            word_freq.update(cleaned_line.split())

    print(f"word frequency: {len(word_freq)}")

    for word, count in word_freq.most_common(15):
        print(f"{word:12} -> {count}")

except FileNotFoundError:  # if file is not found
    print("Error: the file was not found")
except Exception as e:
    print(f"Error reading file: {e}")
