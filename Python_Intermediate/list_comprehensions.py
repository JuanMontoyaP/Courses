def main():
    limit = 99999
    squares = []
    for i in range(1,limit+1):
        squares.append(i**2)
    
    squares_comp =[i**2 for i in range(1,limit+1)]
    # print(squares, squares_comp)

    squares_div = []
    for i in range(1,limit+1):
        if (i % 3 != 0):
            squares_div.append(i**2)

    squares_div_comp = [i**2 for i in range(1,limit+1) if i % 3 != 0]

    # print(squares_div, squares_div_comp)

    ret = [i for i in range(1,limit+1) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    ret_better = [i for i in range(1,limit+1) if i % 36 == 0]
    print(ret_better)

if __name__ == '__main__':
    main()