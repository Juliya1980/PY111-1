from Tasks import a0_my_stack as stack

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    stack.clear()
    for k in brackets_row:
        if k == '(':
            stack.push(')')
        elif k == ')':
            if k != stack.pop():
                return False
    if len(stack.spis_1) != 0:
        return False
    return True

if __name__ == '__main__':
    print(check_brackets(')(())'))
    print(check_brackets('()('))

