import re


def postal_code_generator(postal_code_1, postal_code_2):
    if not re.match("^[0-9]{5}$", postal_code_1) or not re.match("^[0-9]{5}$", postal_code_2):
        raise TypeError("Error! Only 5 digits allowed!")
    postal_code_1, postal_code_2 = int(postal_code_1), int(postal_code_2)

    if postal_code_1 > postal_code_2:
        raise Exception("Error! First postal code has to be lower than second one")

    while postal_code_1 <= postal_code_2:
        if postal_code_1 < 1000:
            yield f'00{postal_code_1}'
        elif postal_code_1 < 10000:
            yield f'0{postal_code_1}'
        else:
            yield postal_code_1
        postal_code_1 += 1


try_me = postal_code_generator('00001', '99999')

for postal_code in try_me:
    print(postal_code)
