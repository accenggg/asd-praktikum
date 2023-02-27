def mergerSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

        # print(f"kiri: {left_data}")
        # print(f"kanan: {right_data}")
        # print(20*"=")

        mergerSort(left_data)
        mergerSort(right_data)   
        
        """
        i = 0 # indeks untuk array kiri
        j = 0 # indeks untuk array kanan
        k = 0 # indeks untuk penggabungannya
        """

        i = j = k = 0

        while i < len(left_data) and j < len(right_data):
            if left_data[i] < right_data[j]:
                data[k] = left_data [i]
                i += 1
            else:
                data[k] = right_data[j]
                j += 1
            k += 1
        
        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1

        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1


data = [2, 8, 10, 7, 5, 1, 3]
print(f"sebelum: {data}")

# proses sorting
mergerSort(data)

# sesudah
print (f"sesudah: {data}")