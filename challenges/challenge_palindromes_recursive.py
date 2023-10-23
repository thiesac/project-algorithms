def is_palindrome_recursive(word, low_index, high_index):
    word = word.lower()
    if word == "":
        return False
    elif high_index - low_index < 1:
        return True
    else:
        return word[low_index] == word[high_index] and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )


# print(is_palindrome_recursive("coxinha", 0, len("coxinha") - 1))
# print(is_palindrome_recursive("radar", 0, len("radar") - 1))
