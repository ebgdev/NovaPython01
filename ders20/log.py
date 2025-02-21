from collections import Counter

with open("log.txt", "r") as file:
    words = file.read().split()

word_counts = Counter(words)
top_words = word_counts.most_common(3)

for word, count in top_words:
    print(f"{word}: {count}")
