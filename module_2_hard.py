number = int(input('Введите любое число от 3 до 20: '))


def get_result(number_):
    result = []

    for i in range(1, number_ + 1):
        for j in range(i + 1, number_ + 1):
            if number_ % (i + j) == 0:
                result.append(str(i))
                result.append(str(j))
    return result


def check_result(number_for_checking, result_for_checking):
    str_ = ''.join(result_for_checking)
    right_combinations = {3: '12',
                          4: '13',
                          5: '1423',
                          6: '121524',
                          7: '162534',
                          8: '13172635',
                          9: '1218273645',
                          10: '141923283746',
                          11: '11029384756',
                          12: '12131511124210394857',
                          13: '112211310495867',
                          14: '1611325212343114105968',
                          15: '1214114232133124115106978',
                          16: '1317115262143531341251161079',
                          17: '11621531441351261171089',
                          18: '12151811724272163631545414513612711810',
                          19: '118217316415514613712811910',
                          20: '13141911923282183731746416515614713812911'
                          }


print('Ваш пароль:', *get_result(number))

check_result(number, get_result(number))
