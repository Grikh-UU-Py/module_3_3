# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return
#1
print_params(a = 15, b=17, c = 2)
print_params(a = 15, b=17)
print_params(a = 13)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
#2
values_list = ['Red', True, 7]
values_dict = {'a':'Blue', 'b':False, 'c':34}
print('--------------------')
print_params(*values_list)
print_params(**values_dict)
#3
print('--------------------')
values_list_2 = [45, True]
print_params(*values_list_2, 42)