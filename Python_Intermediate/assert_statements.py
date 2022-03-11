def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def main():
    num = input("Enter a number: ")
    assert num.isnumeric(), "Must enter a number"
    print(divisors(int(num)))
    print("Done")

if __name__ == "__main__":
    main()