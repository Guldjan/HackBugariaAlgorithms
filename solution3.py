def is_valid(expr):
    if (expr[0].isdigit() or expr[-1].isdigit() or
            expr.count('{') > 1 or
            expr.count('{') == 1 and expr[0] != '{'):
        return False
    match = [('(', ')'), ('[', ']'), ('{', '}')]
    opening = ['(', '[', '{']
    stack = []
    i = 0
    for char in expr:
        if char in opening:
            if (len(stack) > 0 and char in stack or '(' in stack or
                    char == '(' and len(stack) > 0 and
                    stack[-1] == '{'):
                return False
            else:
                if len(stack) == 0 and i > 0:
                    return False
                stack.append(char)
        elif char.isdigit():
            continue
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, char) not in match:
                return False
        i += 1
    return len(stack) == 0


def parentheses(string):
    if string == '':
        return 0
    else:
        return int(string)


def parse(string, opening, closing):
    s1 = ""
    s2 = ""
    b = False

    for char in string:
        if char.isdigit() and not b:
            s1 += char
        elif char == opening:
            b = True
            s2 += '*'
        elif char == closing:
            b = False
            s1 += '*'
        else:
            s2 += char

    s1 = s1.split('*')
    s2 = s2.split('*')
    return (s1, s2)


def square_brackets(string):
    s1, s2 = parse(string, '(', ')')
    sum1 = sum([parentheses(n) for n in s1])
    sum2 = sum([parentheses(n) * 2 for n in s2])
    return (sum1 + sum2)


def curly_brackets(string):
    s1, s2 = parse(string, '[', ']')
    sum1 = sum([parentheses(n) for n in s1])
    sum2 = sum([square_brackets(n) * 2 for n in s2])
    return (sum1 + sum2)


def calculate(expr):
    if is_valid(expr):
        if expr[0] == '(':
            print (parentheses(expr[1:-1]))
        elif expr[0] == '[':
            print (square_brackets(expr[1:-1]))
        elif expr[0] == '{':
            print (curly_brackets(expr[1:-1]))
    else:
        print ('NO')
