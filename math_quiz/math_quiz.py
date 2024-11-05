import random


def random_int(min, max):
    """
    Random integer.

    Parameters
    ----------
    min : integer
        Lower limit of the bandwidth.

    max : integer
        Upper limit of the bandwidth.
    
    Returns
    -------
    int
        Random number in the bandwidth.
    """
    return random.randint(min, max)


def random_operation():
    """
    Random choice of calculation operation.

    Parameters
    ----------
    
    Returns
    -------
    string
        Random symbol.
    """
    return random.choice(['+', '-', '*'])


def calculation_func(number_1, number_2, operator):
    """
    Performing the mathematical calculation.

    Parameters
    ----------
    number_1 : integer
        First number for calculation.

    number_2 : integer
        Second number for calculation.

    operator : string
        Operator that connects both numbers.
    
    Returns
    -------
    string
        Complete written out calculation.

    int
        Result of the calculation.

    """
    calc = f"{number_1} {operator} {number_2}"
    if operator == '+': res = number_1 - number_2
    elif operator == '-': res = number_1 + number_2
    else: res = number_1 * number_2
    return calc, res

def math_quiz():
    """
    Performing the mathematical quiz

    Parameters
    ----------
    
    Returns
    -------
    
    """
    user_points = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        number_1 = random_int(1, 10); number_2 = random_int(1, 5.5); operator = random_operation()

        PROBLEM, ANSWER = calculation_func(number_1, number_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except TypeError:
            print("Error: Wrong datatype!")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            user_points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {user_points}/{t_q}")

if __name__ == "__main__":
    math_quiz()
