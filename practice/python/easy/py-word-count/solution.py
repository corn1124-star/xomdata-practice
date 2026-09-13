# Xom Data · Count words in a paragraph
# Problem: https://xomdata.com/practice/py-word-count
# Solved: 2026-09-13

def count_words(sentence):
    if not sentence or not sentence.replace(" ", "").isalpha():
        return 0
    return len(sentence.split())
