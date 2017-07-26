speed = 70
is_birthday = True

if speed < 31 and not(is_birthday):
    print('no ticket')
elif speed > 30 and speed < 51 and not(is_birthday):
    print('small ticket')
elif speed > 50 and not(is_birthday):
    print('big ticket')
elif speed < 36 and is_birthday:
    print('no ticket')
elif speed > 35 and speed < 56 and is_birthday:
    print('small ticket')
else:
    print('big ticket')
