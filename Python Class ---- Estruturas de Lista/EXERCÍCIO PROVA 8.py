def first(word):
    return word[0]
def last(word):
    return word[-1]
def midlle(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(first("Douglas"))
print(last("Douglas"))
print(midlle("kaiak"))
