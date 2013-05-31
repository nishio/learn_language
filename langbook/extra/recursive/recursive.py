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
    is_function_call = True
    # gotoのない言語で「関数冒頭へのジャンプ」に相当することを実現するためにwhileを使う
    while True:
        if is_function_call: # 関数呼び出し時だけTrueになるフラグ
            # 初期化
            result = 0
            i = 0
            is_function_call = False

        # for文に相当
        while i < len(xs):
            x = xs[i]
            i += 1
            if is_integer(x):
                result += x
            else:
                ## 関数呼び出しに相当することをやる
                # 今の状態をスタックに積む
                stack.append((xs, i, result))
                # xsを変える(xを引数としてtotalを呼ぶことに相当)
                xs = x
                # ここで関数冒頭へgotoしたいところだがPythonにはgotoがないので
                # フラグを立ててbreakする
                is_function_call = True
                break

        # whileを抜けた際、ループが普通に終了した場合と、関数呼び出しのためにbreakしたのを区別する必要がある
        if is_function_call:
            # 関数呼び出しの場合、何もせずにcontinueすることでwhile冒頭へのジャンプを行う
            continue
        else:
            # 関数呼び出しでない場合

            # 元の関数のループの後に何らかの処理があるならばここに入るが、今回はたまたま
            # 何もせずにreturn resultで抜けているのでここに入る処理はない。

            # 関数を抜けた後の処理
            if not stack: # スタックが空なら
                return result # すべての計算が完了したのでこの関数から抜ける

            # スタックが積まれている場合、中断していた処理を再開する必要がある。
            # 積んでおいた値を取り出す
            old_xs, old_i, old_result = stack.pop()
            # 値を元に戻す
            xs = old_xs
            i = old_i
            result = old_result + result # result += total(x)で返り値を足していることに相当
            # この後、while冒頭に戻って、 is_function_call == False なので初期化処理を飛ばして
            # 2つ目のwhileに戻るので結果的に「再開」ができる。

    return result

print total([1, [2, 3], 4])
print total2([1, [2, 3], 4])
print total3([1, [2, 3], 4])
print total([1, [2, 3], 4, [1, [2, 3], 4]])
print total2([1, [2, 3], 4, [1, [2, 3], 4]])
print total3([1, [2, 3], 4, [1, [2, 3], 4]])
