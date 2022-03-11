def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def main():
    print(is_palindrome("Ana"))

if __name__ == "__main__":
    main()

# mypy palindrome.py --check-untyped-defs