from functools import reduce


def main():
    palindrome = lambda string: string == string[::-1]

    def palindrome_fun(string):
        return string == string[::-1]

    print(palindrome('ana'))

    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd)

    squares = list(map(lambda x: x**2, my_list))
    print(squares)

    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a*b, my_list)
    print(all_multiplied)


if __name__ == '__main__':
    main()