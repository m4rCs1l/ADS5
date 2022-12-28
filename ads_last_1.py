st = input('Введите последовательность скобок: ').strip()

nums_o = []
nums_c = []

if st.count(')')+st.count('(') != len(st):
    print('FUCK U')
elif st[0] == ')':
    print('NUMBA ONE')
elif ')' not in st:
    print('NUMBA ONE')
else:
    nums_o = [c for c in range(len(st)) if st[c] == '(']
    nums_c = [z for z in range(len(st)) if st[z] == ')']
    while len(nums_o) != 0 and len(nums_c) != 0:
        if nums_o[0] < nums_c[0]:
            nums_o.pop(0)
            nums_c.pop(0)
        else:
            break
    if len(nums_o) != 0 and len(nums_c) != 0:
        print(f'NUMBA {min(nums_o[0], nums_c[0]) + 1} IS WRONG')
    elif len(nums_o) == 0 and len(nums_c) == 0:
        print(f'DA {st} IS A GOOD BOY')
    else:
        try:
            print(f'NUMBA {nums_o[0] + 1} IS WRONG')
        except IndexError:
            print(f'NUMBA {nums_c[0] + 1} IS WRONG')








