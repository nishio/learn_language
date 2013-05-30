# -*- coding: utf-8 -*-

def is_integer(x):
    return isinstance(x, int)

def total(xs):
    result = 0
    for x in xs:
        if is_integer(x):
            result += x
        else:
            result += total(x)

    return result


def total2(xs):
    # 初期化
    result = 0
    i = 0

    # for文に相当
    while i < len(xs):
        x = xs[i]
        i += 1
        if is_integer(x):
            result += x
        else:
            result += total(x)

    return result


def total3(xs):
    stack = []
    # 初期化
    result = 0
    i = 0

    # 再帰呼び出しでの「関数冒頭へのジャンプ」に相当
    while True:

        # for文に相当
        while i < len(xs):
            x = xs[i]
            i += 1
            if is_integer(x):
                result += x
            else:
                # 今の状態をスタックに積む
                stack.append((xs, i, result))
                # xsを変える(xを引数としてtotalを呼ぶことに相当)
                xs = x
                # 初期化
                result = 0
                i = 0
                break

        if i == len(xs):
            # ループが完了した
            if stack: # スタックが空でないなら
                # 積んでおいた値を取り出す
                old_xs, old_i, old_result = stack.pop()
                # 値を元に戻す
                xs = old_xs
                i = old_i
                result = old_result + result # result += total(x)で返り値を足していることに相当
            else:
                break

    return result

print total([1, [2, 3], 4])
print total2([1, [2, 3], 4])
print total3([1, [2, 3], 4])
print total([1, [2, 3], 4, [1, [2, 3], 4]])
print total2([1, [2, 3], 4, [1, [2, 3], 4]])
print total3([1, [2, 3], 4, [1, [2, 3], 4]])
