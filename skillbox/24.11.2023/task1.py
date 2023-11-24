import re

def validate_password(password):

    # Проверка содержит ли пароль только латинские символы, цифры и специальные символы ^$%@#&*
    if not re.match(r'^[a-zA-Z0-9^$%@#&*]+$', password):
        return False

    # Проверка что длина пароля должна быть больше 8
    if len(password) < 8:
        return False

    # Проверка содержит ли пароль хотя бы 2 строчных латинских символа
    if not re.search(r'[a-z].*[a-z]', password):
        return False

    # Проверка есть ли цифры в пароле
    if not re.search(r'\d', password):
        return False

    # Проверка содержит ли пароль хотя бы 3 разных специальных символа
    if len(set(re.findall(r'[^\w\s]', password))) < 3:
        return False

    return True

def run_tests():

    # Верные пароли
    assert validate_password("rtG&3FG#Tr^e") == True
    assert validate_password("a^A1@*@1Aa") == True
    assert validate_password("oF^a1D@y5%e6") == True
    assert validate_password("enroi#$*rkdeR#$*092uwedchf34tguv394h") == True

    # Неподходящие пароли
    assert validate_password("пароль") == False
    assert validate_password("password") == False
    assert validate_password("qwerty") == False
    assert validate_password("lOngPa$$W0Rd") == False

    print("All tests passed!")

run_tests()