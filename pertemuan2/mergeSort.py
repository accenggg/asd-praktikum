def merge_sort (array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array [mid:]

        # print(f"left: {left_arr}")
        # print(f"right: {right_arr}")
        # print(20*"=")

        # rekursif
        merge_sort(left_arr)
        merge_sort(right_arr)

        # penggabungan array
        """
        i = 0 # indeks untuk array kiri (left_arr)
        j = 0 # indeks untuk array kanan (right_arr)
        k = 0 # indeks untuk penggabungan
        """

        # bisa disingkat dengan
        i = j = k = 0
        
        # array kiri dan array kanan masih ada
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
                # k += 1
            else:
                array[k] = right_arr[j]
                j += 1
                # k += 1
            k += 1

        # array kiri masih ada namun array kanan sudah habis
        while (i < len(left_arr)):
            array[k] = left_arr[i]
            i += 1
            k += 1
        
        # array kanan mmasih ada namun array kiri sudah habis
        while (j < len(right_arr)):
            array[k] = right_arr[j]
            j += 1
            k += 1

array = [2,3,2,2,5,9,2,1,5,829,204,183,1,3]
merge_sort (array)
print(array)
