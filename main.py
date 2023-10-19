#def func(lst): return list(map(lambda x: None if not x.isdigit() else x,list(map(str,lst))))
#def func2(lst): return list(map(lambda x: int(x) if x else x,lst))
#print(func2(func(['1',[],'()','{}'])))



#def list_insert():
#    ref_list = [0, 1, 2, 3, 4, 5]
#    start = 4
#    num = 40
#    rep = 2
#    stop = 2
#    ref_list = [3, 4, 5, 1, 7]
#    print(ref_list)






d = {
    1: '1',
    '2': 2,
    3: '3',
}


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

print(get_key(d, '1'))
print(get_key(d, 2))
print(get_key(d, 42))








