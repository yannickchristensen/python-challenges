def capital_indexes(word):
    list = []
    for letter in word:
        if letter.isupper():
            list.append(word.index(letter))
    return list

print(capital_indexes('HeLlO'))