import re

text = '+7 499 457-45-78' \
       '+74994574578' \
       '7 (499) 457 45 78' \
       '7 (499) 457-45-78'

reg = r'\+?7\s?\(?\d{3}\)?\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}'

print(re.findall(reg, text))

passwords = ('p@ssWord-', 'psw', 'psw+_asfw', 'P@ASSworD')


def check_pass(pass_w):
    return re.findall(r'[A-z0-9@_-]{6,18}$', pass_w)


print(check_pass(passwords[0]))
print(check_pass(passwords[1]))
print(check_pass(passwords[2]))
print(check_pass(passwords[3]))
