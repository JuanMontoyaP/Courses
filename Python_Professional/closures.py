def make_repeater_of(n: int):
    def repeater(string: str) -> str:
        assert type(string) == str, "Just Strings"
        return string * n
    return repeater

def main():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hi"))

if __name__ == '__main__':
    main()