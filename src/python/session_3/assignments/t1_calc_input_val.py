"""Simple command-line calculator with clear error handling. Note: refactoring is needed"""


def add(num_1: float, num_2: float) -> float:
    """
    This function adds up two floating point number

    :param num_1: first operand
    :type num_1: float

    :param num_2: second operand
    :type num_2: float

    :returns: the sum of the given numbers
    :rtype: float
    """
    return num_1 + num_2


def sub(num_1: float, num_2: float) -> float:
    """
    This function subtracts two floating point number

    :param num_1: first operand
    :type num_1: float

    :param num_2: second operand
    :type num_2: float

    :returns: the difference between the given numbers
    :rtype: float
    """
    return num_1 - num_2


def div(num_1: float, num_2: float) -> float:
    """
    This function divides two floating point number

    :param num_1: first operand
    :type num_1: float

    :param num_2: second operand
    :type num_2: float

    :returns: the division of the given numbers
    :rtype: float
    """
    return num_1 / num_2


def multiply(num_1: float, num_2: float) -> float:
    """
    This function multipliestwo floating point number

    :param num_1: first operand
    :type num_1: float

    :param num_2: second operand
    :type num_2: float

    :returns: the multiplication of the given numbers
    :rtype: float
    """
    return num_1 * num_2


def main() -> None:
    operation_mapping = {1: "+", 2: "-", 3: "/", 4: "*"}

    print("---------Calculator---------")
    print("Choose an operation:")
    print("1-sum")
    print("2-sub")
    print("3-div")
    print("4-mul")
    print("5-exit")

    while True:
        try:
            try:
                choice = int(input("Enter the operation: "))
                num_1 = float(input("Enter first num: "))
                num_2 = float(input("Enter second num: "))

            except ValueError:
                print("Only NUMERIC values are allowed\n")

            else:
                if (choice > 4 or choice < 1) and (choice != 5):
                    print("Invalid choice, try again or exit\n")
                    continue

                elif choice == 5:
                    print("Thanks for using the calculator, Bye")
                    return

                else:
                    if choice == 1:
                        result = add(num_1, num_2)

                    elif choice == 2:
                        result = sub(num_1, num_2)

                    elif choice == 3:
                        try:
                            result = div(num_1, num_2)

                        except ZeroDivisionError:
                            print("Division by ZERO is NOT allowed\n")
                            continue

                    elif choice == 4:
                        result = multiply(num_1, num_2)

                    print(
                        f"{num_1} {operation_mapping[choice]} {num_2} = {result}\n\n{'-' * 30}"
                    )

        except Exception as e:
            print(f"That's Awkward and Error happened:{e}")


if __name__ == "__main__":
    main()
