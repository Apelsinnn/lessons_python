# Написать функцию проверки "силы" пароля, возвращает всегда строку
# -если пароль короче 8 символов, то вернуть Too weak
# -если пароль содержит только цифры, только строчные, только заглавные, то вернуть Weak
# -если пароль содержит символы любых 2 наборов, вернуть Good
# -если пароль содержит символы любых 3 наборов, вернуть Very good
import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return 'Weak'
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Very good'
    return 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('asdfghj') == 'Too Weak'
    assert password_strength('ASDFGHJ') == 'Too Weak'
    assert password_strength('AsDfGhj') == 'Too Weak'
    assert password_strength('123ASD') == 'Too Weak'
    assert password_strength('123asd') == 'Too Weak'
    assert password_strength('12as12A') == 'Too Weak'
    assert password_strength('123456789000000000000000000000000000000000000000000000000000000000000') == 'Weak'
    assert password_strength('123456789') == 'Weak'
    assert password_strength('asdfghhjk') == 'Weak'
    assert password_strength('ASDFGHJKL') == 'Weak'
    assert password_strength('123aa456asda22sd') == 'Good'
    assert password_strength('123DD456ASDA11SD') == 'Good'
    assert password_strength('asAAdasdASaaDASD') == 'Good'
    assert password_strength('asdasdASDASD123123') == 'Very good'
    assert password_strength('asdASDasdASDasdASD123DDD123') == 'Very good'
    assert password_strength('asdA123SDasdASDa123sdASD123DDD123') == 'Very good'
