# 逆波兰解释器


def isOp(s):
    return s == '+' or s == '-'


def op(first, second, op):
    result = eval(str(first) + op + str(second))
    print(type(result))
    return result


def evalRPN(rpn):
    stack = []
    for item in rpn:
        if item.isdigit():
            stack.append(item)
        elif isOp(item):
            second = stack.pop()
            first = stack.pop()
            r = op(first, second, item)
            stack.append(r)
    return int(stack.pop())


rpn = ['1', '2', '+', '6', '-']
print(evalRPN(rpn))
