from collections import Counter


def top_k_frequent(words: list[str], k: int) -> list[str]:
    counter = Counter(words)
    # Sort by (-frequency, word) to get descending frequency and lex ascending
    sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, _ in sorted_words[:k]]


print(top_k_frequent(["apple", "banana", "apple", "orange", "banana", "apple"], 2))
# Output: ["apple", "banana"]


print(top_k_frequent(["dog", "cat", "dog", "rat", "cat", "dog"], 3))
# Output: ["dog", "cat", "rat"]
