def is_palindrome(word: str) -> bool:
    # approach taken:
    # case neutralize and reverse word. then compare original vs outcome
    rev_word = word[::-1]
    return word.casefold() == rev_word.casefold()


print(is_palindrome(input('Enter possible palindrome: \n')))

