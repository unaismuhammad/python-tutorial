def sum_list(1st):
    if not 1st:
        return 0
        else:
            return 1st[0]+sum_list([1:])
            print(sum_list([1,2,3,4,5]))