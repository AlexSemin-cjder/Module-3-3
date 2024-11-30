
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = [[3, 4, 5], 'Alex', 123]
values_dict = {'a': 123, 'b': [5, 6, 7], 'c': 'Alex'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)