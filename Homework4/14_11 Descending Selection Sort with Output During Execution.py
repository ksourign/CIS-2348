#Kaitlyn Sourignosack
#1824497

def selection_sort_descend_trace(list):

    N = len (list) -1

    for i in range(0,N):
        max = i
        for j in range (i+1, len (list)):
            if list [j] > list [max]:
                max = j

            if j == N and max != i:
                list [max], list [i] = list [i], list[max]
        for q in list:
            print (f'{q} ', end='')
        print ()

if __name__ == '__main__':
    lista = []
    a =  (input())
    split_list = a.split()


    for i in range (len(split_list)):
        split_list[i] = int (split_list [i])

    selection_sort_descend_trace(split_list)
