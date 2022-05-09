# vowels = ['a', 'o', 'u', 'e', 'i']
# text = input()
# no_vows = []
# for ch in text:
#     if ch not in vowels:
#         no_vows.append(ch)
# print(''.join(no_vows))

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vows = [ch for ch in text if ch not in vowels]
print(''.join(no_vows))
