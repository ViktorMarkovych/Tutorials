from tutorials import sorting_bubble



def test_sorting_bubble():
    arr = [5, 5, 7, 8, 2, 4, 1]
    sorting_bubble.bubble_sort(arr)
    assert arr == [1, 2, 4, 5, 5, 7, 8], 'bad sorting'

def test_sorting_bubble_1():
    arr = [0, 78, 55, 6, 2, -5, -1]
    sorting_bubble.bubble_sort(arr)
    assert arr == [-5, -1, 0, 2, 6, 55, 78], 'bad sorting'