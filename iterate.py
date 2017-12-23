#!/usr/bin/env python

import re


def poly(tokens):
    sum = None
    op = None
    for t in tokens:
        # 第一个直接赋值
        if not sum:
            sum = int(t)
            continue
        if t == '+' or t == '-':
            # 如果是符号则缓存
            op = t
        else:
            # 计算表达式并缓存
            if op == '+':
                sum += int(t)
            elif op == '-':
                sum -= int(t)
    return sum


def evalExp(exp):
    pattern = re.compile(regex)
    tokens = pattern.findall(exp)
    return poly(tokens)


regex = r'([0-9]+|[+-])'

if __name__ == "__main__":
    input = "123+24-5+6"
    r = evalExp(input)
    print(r)
