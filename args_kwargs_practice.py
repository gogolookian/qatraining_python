def arg(*args):
    print(type(args))
    for i in args:
        print(i)

def kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key + "=" + value)


if __name__ == '__main__':
    # name_dic = {'name1': 'Ian', 'name2': 'Flower', 'name3': 'Momoko', 'name4': 'Caspar', 'name5': 'Patricia'}
    # a_dic = {'1': 1}

    a_list = [1, 2]
    el = a_list.pop(1)
    print(el)
    print(a_list)
    #
    # pick_1_3_5 = name_list[0:5:2]
    # name = 'Patricia'
    # number = 13579
    # pick_1_3_5 = number[0:5:2]
    # print(pick_1_3_5)
    # for item in name_dic.items():
    #     print(item)
    # name1 = name_dic['name1']

    # value = name_dic.setdefault('name9', default='AAA')
    # name = name_dic.setdefault('name9', "no one")

    # name_dic.update(a_dic)
    # print(name_dic)