def is_palindrome_iterative(word):
    word = word.lower()
    if word == "":
        return False

    low = 0
    high = len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True


# Test the function
print(is_palindrome_iterative("coxinha"))
print(is_palindrome_iterative("radar"))
