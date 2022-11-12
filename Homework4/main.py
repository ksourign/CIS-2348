#Kaitlyn Sourignosack
#1824497

num_calls = 0

def partition(user_ids, i, k):

    low = i
    hi = k
    midPoint = i + (k - i) // 2
    pivot = user_ids[midPoint]

    count = 0

    while count == 0:
        while user_ids[low] < pivot:
            low += 1
        while pivot < user_ids[hi]:
            hi -= 1

        if low >= hi:
            count += 1
        else:
            user_ids[low], user_ids[hi] = user_ids[hi], user_ids[low]

            low += 1
            hi -= 1

    return hi




def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return

    z = partition(user_ids, i, k)
    quicksort(user_ids, i, z)
    quicksort(user_ids, z + 1, k)



if __name__ == "__main__":

    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)