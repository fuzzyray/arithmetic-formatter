def arithmetic_arranger(problems, solve=False):

    # Number of problems is limited to 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # Split problems into individual problems
    for problem in problems:
        [operand1, operator, operand2] = problem.split()

        # Check operators
        if operator not in '+-':
            return "Error: Operator must be '+' or '-'."

        # Check that input is comprised of digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check that numbers are 4 digits or less
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

    arranged_problems = ''

    return arranged_problems
