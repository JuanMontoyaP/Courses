def make_division_by(n: int):
    def division(x: int) -> float:
        return x / n
    return division

# def make_division_lambda(n: int):
#     return lambda x: x/n

def main():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

if __name__ == "__main__":
    main()