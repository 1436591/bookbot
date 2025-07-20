def word_count(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def char_count(text):
    words = text.split()
    lower_words = []
    chars = [      
        {"name": "a", "num": 0},
        {"name": "b", "num": 0},
        {"name": "c", "num": 0},
        {"name": "d", "num": 0},
        {"name": "e", "num": 0},
        {"name": "f", "num": 0},
        {"name": "g", "num": 0},
        {"name": "h", "num": 0},
        {"name": "i", "num": 0},
        {"name": "j", "num": 0},
        {"name": "k", "num": 0},
        {"name": "l", "num": 0},
        {"name": "m", "num": 0},
        {"name": "n", "num": 0},
        {"name": "o", "num": 0},
        {"name": "p", "num": 0},
        {"name": "q", "num": 0},
        {"name": "r", "num": 0},
        {"name": "s", "num": 0},
        {"name": "t", "num": 0},
        {"name": "u", "num": 0},
        {"name": "v", "num": 0},
        {"name": "w", "num": 0},
        {"name": "x", "num": 0},
        {"name": "y", "num": 0},
        {"name": "z", "num": 0},
        ]
    for word in words:
        lower_words.append(word.lower())
    for word in lower_words:
        for char in word:
            for c in chars:
                if char == c["name"]:
                    c["num"] += 1
    return chars

def sort_dic(text):
    chars = char_count(text)
    chars.sort(reverse=True, key=sort_on)
    return chars

