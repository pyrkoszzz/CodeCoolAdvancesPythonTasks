from string import punctuation

def check_if_palindrome(text: str) -> bool:
    text = ''.join(text.lower().translate(str.maketrans('', '', punctuation)).split())
    return text == text[::-1]
