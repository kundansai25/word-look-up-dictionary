import tkinter as tk
from tkinter import messagebox
from trie import Trie
from utils import correct
from scraper import get_meaning

# Sample dictionary for testing
sample_words = ["apple", "banana", "grape", "mango", "orange", "pineapple", "watermelon"]

# Load dictionary into Trie
trie = Trie()
for word in sample_words:
    trie.insert(word)

# GUI
def search_word():
    word = entry.get().strip()
    if trie.search(word):
        meaning = get_meaning(word)
        result_label.config(text=f"✓ Found!\nMeaning: {meaning}")
    else:
        suggestions = trie.suggest(word[:2])
        correction = correct(word, sample_words)
        result_label.config(
            text=f"✗ Word not found!\nSuggestions: {', '.join(suggestions[:5])}\nDid you mean: {correction}?"
        )

root = tk.Tk()
root.title("Word Lookup Dictionary")

tk.Label(root, text="Enter Word:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Search", command=search_word).pack(pady=5)
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()