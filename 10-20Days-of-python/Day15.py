movies = ["Kantara", "KGF", "777 Charlie", "Garuda Gamana Vrishabha Vahana", "Kirik Party"]

movie_iterator = iter(movies)

print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))


class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 2
            return value
        else:
            raise StopIteration


numbers = EvenNumbers(10)

for num in numbers:
    print(num)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)

import sys

list_numbers = [x for x in range(1, 1000001)]

generator_numbers = (x for x in range(1, 1000001))

print("List size:", sys.getsizeof(list_numbers))
print("Generator size:", sys.getsizeof(generator_numbers))
