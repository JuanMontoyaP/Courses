def main():
    limit = 100
    my_dict = {}

    for i in range(1,limit+1):
        if i % 3 != 0:
            my_dict[i] = i**3

    my_dict_comp = {i: i**3 for i in range(1,limit+1) if i % 3 != 0}
    # print(my_dict_comp)

    my_dict_ret = {i: i**0.5 for i in range(1,limit+1)}
    print(my_dict_ret)

if __name__ == '__main__':
    main()