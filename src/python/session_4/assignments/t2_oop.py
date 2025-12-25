from typing import Any, Set, List


class Fibonacci:
    """
    A class to generate fibonacci numbers

    Attributes:
        n (int): number of fibonacci numbers to be calculated
    """

    def __init__(self, n: int) -> None:
        self.n = n

    def generate(self) -> List[int]:
        """
        This function calculates the first `n` fibonacci numbers

        :param n: number of fibonacci numbers to be calculate
        :type n: int

        :return: a list containing the first n fibonacci numbers
        :rtype: List[int]
        """

        if self.n <= 1:
            return [self.n]

        fib = [0, 1]

        for i in range(2, self.n):
            fib.append(fib[-1] + fib[-2])

        return fib


# f = Fibonacci(10)
# fib_list = f.generate()
# print(fib_list)


class SetElementRemover:
    """
    A class to remove elements from a set

    Attributes:
        input_set (set): the input set from which elements will be removed
    """

    def __init__(self, input_set: Set[Any]) -> None:
        self.input_set = input_set

    def remove_element(self, item: Any) -> Set[Any]:
        """
        This function removes specified elements from the input set

        :param item: an element to be removed from the set
        :type item: Any

        :return: the modified set after removing specified elements
        :rtype: set
        """

        try:
            self.input_set.remove(item)

        except KeyError:
            print("Element not in set, no change in set:")

        return self.input_set

    def remove_elements(self, input_set: Set[Any], *items: Any) -> Set[Any]:
        """
        Removes multiple items from a set.

        :param input_set: The set to remove items from.
        :type input_set: Set[Any]
        :param items: The items to remove.
        :type items: Any
        :return: The modified set.
        :rtype: Set[Any]
        """

        for item in items:
            try:
                input_set.remove(item)
            except KeyError:
                print(f"{item} doesn't exist in set, skipping...")

        return input_set


# ser = SetElementRemover({1, 2, 3, 4, 5})
# ser.remove_element(item=2)
# print(ser.input_set)
# print(ser.remove_elements(ser.input_set, 3, 6, 1))


class TupleIndexFinder:
    """
    A class to find indices of elements in a tuple

    Attributes:
        input_tuple (tuple): the input tuple in which indices will be searched
    """

    def __init__(self, input_tuple: tuple) -> None:
        self.input_tuple = input_tuple

    def find_index(self, item: Any) -> int:
        """
        This function finds the index of a specified element in the input tuple

        :param item: an element whose index is to be found
        :type item: Any

        :return: the index of the specified element
        :rtype: int
        """

        try:
            index = self.input_tuple.index(item)
            return index

        except ValueError:
            print("Element not found in tuple")
            return -1


# tif = TupleIndexFinder((10, 20, 30, 40, 50))
# print(tif.find_index(30))
# print(tif.find_index(60))


class WordTokenizer:
    """
    A class to tokenize	 a sentence into words

    Attributes:
       sentence (str): the input sentence to be tokenized
    """

    def __init__(self, sentence: str) -> None:
        self.sentence = sentence

    def tokenize(self) -> List[str]:
        """
        Tokenizes a sentence into words.

        :param sentence: The sentence to tokenize.
        :type sentence: str
        :return: A list of words.
        :rtype: List[str]
        """

        return self.sentence.split()


# wt = WordTokenizer("This is an example sentence for tokenization.")
# print(wt.tokenize())


class PalindromeChecker:
    """
    A class to check if a string is a palindrome
    """

    def __init__(self) -> None:
        pass

    def is_palindrome(self, s: str) -> bool:
        """
        Checks if the input string is a palindrome.

        :param input_string: The string to check.
        :type input_string: str
        :return: True if the string is a palindrome, False otherwise.
        :rtype: bool
        """

        is_pal = s == s[::-1]
        return is_pal


# pc = PalindromeChecker()
# print(pc.is_palindrome("racecar"))
# print(pc.is_palindrome("hello"))


class FactorialGenerator:
    """
    A class to generate fibonacci numbers using generator
    """

    def __init__(self) -> None:
        pass

    def generate(self, n: int) -> int:
        """
        Generates fibonacci numbers up to n.

        :param n: The number of fibonacci numbers to generate.
        :type n: int
        :return: The next fibonacci number.
        :rtype: int
        """

        if n == 0 or n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i

        return result


# fg = FactorialGenerator()
# print(fg.generate(5))
# print(fg.generate(10))


class Squares:
    """
    A class to generate squares of numbers using generator
    """

    def __init__(self, n: int = 10) -> None:
        self.n = n

    def generate(self):
        """
        Generates squares of numbers up to n.

        :param n: The number of squares to generate.
        :type n: int
        :return: The next square number.
        :rtype: int
        """

        return [i**2 for i in range(1, self.n + 1)]


# sq = Squares(10)
# print(sq.generate())


class SquaresAnotherSolution:
    """
    A class to generate squares of numbers using generator

    Attributes:
        n (int): The number up to which squares are to be generated, default is 10.
    """

    def __init__(self, n: int = 10) -> None:
        self.n = n

    def generate(self) -> List[int]:
        """
        Generates a list of squares of numbers from 1 to n.

        :return: A list of squares.
        :rtype: List[int]
        """
        sq_lst = []

        for i in range(1, self.n + 1):
            sq_lst.append(i**2)

        return sq_lst


# sq_another = SquaresAnotherSolution(10)
# print(sq_another.generate())


class SumOfEvens:
    """
    A class to calculate the sum of even numbers in a given list

    Attributes:
       lst (List[int]): The list of integers to process.
    """

    def __init__(self, lst: List[int]) -> None:
        self.lst = lst

    def calculate(self) -> int:
        sum = 0

        for num in self.lst:
            if num % 2 == 0:
                sum += num

        return sum


# soe = SumOfEvens([1, 2, 3, 4, 5, 6])
# print(soe.calculate())


class ReverseList:
    """
    A class to reverse a given list

    Attributes:
        lst (List[Any]): The list to be reversed.
    """

    def __init__(self, lst: List[Any]) -> None:
        self.lst = lst

    def reverse(self) -> List[Any]:
        """
        Reverses the input list.

        :return: The reversed list.
        :rtype: List[Any]
        """

        return self.lst[::-1]


# rl = ReverseList([1, 2, 3, 4, 5])
# print(rl.reverse())


class MedianCalculator:
    """
    A class to calculate the median of a list of numbers

    Attributes:
       numbers (List[float]): The list of numbers to calculate the median for.
    """

    def __init__(self, numbers: List[float]) -> None:
        self.numbers = numbers

    def calculate(self) -> float:
        """
        Calculates the median of the list of numbers.

        :return: The median value.
        :rtype: float
        """

        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        mid = n // 2

        if n % 2 == 0:
            median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            median = sorted_numbers[mid]

        return median


# mc = MedianCalculator([3, 1, 4, 4, 2, 5])
# print(mc.calculate())


class ModeCalculator:
    """
    A class to calculate the mode of a list of elements

    Attributes:
        lst (List[Any]): The list of numbers to calculate the mode for.
    """

    def __init__(self, lst: List[Any]) -> None:
        self.lst = lst

    def calculate(self) -> Any:
        """
        Calculates the mode of the list of elements.

        :return: The mode value.
        :rtype: Any
        """

        frequency = {}

        for item in self.lst:

            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        mode = max(frequency.keys(), key=lambda k: frequency[k])

        return mode


# modecalc = ModeCalculator([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5])
# print(modecalc.calculate())


class Grader:
    """
    A class to assign grades based on scores

    Attributes:
        mark (float): The mark to be graded.
    """

    def __init__(self, mark: float) -> None:
        self.mark = mark

    def assign_grade(self) -> str:
        """
        Converts a numerical mark to a letter grade.

        :param mark: The numerical mark.
        :type mark: float
        :return: The corresponding letter grade.
        :rtype: str
        """

        if self.mark >= 85 and self.mark <= 100:
            return "A"
        elif self.mark >= 75 and self.mark < 85:
            return "B"
        elif self.mark >= 65 and self.mark < 75:
            return "C"
        elif self.mark >= 50 and self.mark < 65:
            return "D"
        else:
            return "F"


# grader = Grader(88)
# print(grader.assign_grade())
# grader = Grader(50)
# print(grader.assign_grade())
