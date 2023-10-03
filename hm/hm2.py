text = 'Ежевику для ежат ' \
       'Принеси два ежа. ' \
       'Ежевику еле-еле ' \
       'Ежата возле ели съели.'
print(text)
text_arr = text.split(' ')
count = 0
for i in text_arr:
    if i[0] == 'е' or i[0] == 'Е':
        count += 1

print('Первых букв "Е":', count)
