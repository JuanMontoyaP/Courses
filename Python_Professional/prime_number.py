def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    else :
        divisors: int = 0
        for i in range(2, number):
            if (number % i == 0):
                divisors += 1
        if divisors != 0:
            return False
        else :
            return True

def main():
    print(is_prime(3))
    print(is_prime(2))
    print(is_prime(5))
    print(is_prime(10))
    print(is_prime(15))
    print(is_prime(21))

if __name__ == '__main__':
    main()