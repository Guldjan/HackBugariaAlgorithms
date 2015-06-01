def is_palindrome(word):
    return word == word[::-1]


def rotations(word):
    return [word[i:] + word[:i] for i in range(len(word))]


def print_palindrome_rotations(word):
    if not([print(w) for w in rotations(word) if is_palindrome(w)]):
        print('NONE')
