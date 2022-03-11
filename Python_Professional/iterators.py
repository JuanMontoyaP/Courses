import time

class FiboIter():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.aux = 0
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1  
            if self.max != 0:
                return self.n2
            else: 
                raise StopIteration
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if not self.max or self.aux <= self.max:
                return self.aux
            else:
                raise StopIteration
    

if __name__ == "__main__":
    fibonacci_1 = FiboIter(0)
    for element in fibonacci_1:
        print(element)
        time.sleep(0.5)

    print("---------------------------------------------")
    
    fibonacci_2 = FiboIter(1)
    for element in fibonacci_2:
        print(element)
        time.sleep(0.5)

    print("---------------------------------------------")

    fibonacci_3 = FiboIter(20)
    for element in fibonacci_3:
        print(element)
        time.sleep(0.5)

    print("---------------------------------------------")

    fibonacci_4 = FiboIter()
    for element in fibonacci_4:
        print(element)
        time.sleep(0.5)