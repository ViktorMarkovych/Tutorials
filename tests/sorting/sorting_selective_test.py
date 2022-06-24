from tutorials import sorting_selective



def selective_sort_test():
    arr = [5, 6, 7, 8, 2, 4, 1]
    sorting_selective.selective_sort(arr)
    assert arr == [1, 2, 4, 5, 6, 7, 8], 'bad sorting'

def selective_sort_test_1():
    arr = [-5, 106, 7, 5, 10, -4, 0]
    sorting_selective.selective_sort(arr)
    assert arr == [-5, -4, 0, 5, 7, 10, 106], 'bad sorting'