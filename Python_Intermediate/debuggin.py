def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def main():
    try:
        num = int(input("Enter a number: "))
        if (num < 0):
            raise ValueError("Negative Number")
        print(divisors(num))
        print("Done")
    except ValueError as ve:
        print(ve)
        print("Must enter a valid number")

if __name__ == "__main__":
    main()