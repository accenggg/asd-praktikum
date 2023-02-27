def shell_sort(arr):
    n = len(arr) # Mendapatkan panjang array
    gap = n // 2 # Set nilai gap sebesar n/2

    while gap > 0: # Selama nilai gap lebih besar dari 0, lakukan sorting
        for i in range(gap, n): # Loop sebanyak gap hingga n
            temp = arr[i] # Simpan nilai array pada index i pada variabel temp
            j = i # Inisiasi variabel j sama dengan i
            
            while j >= gap and arr[j - gap] > temp: # Selama nilai j lebih besar atau sama dengan gap dan nilai pada index arr[j-gap] lebih besar dari nilai temp, lakukan pengurutan secara Insertion Sort
                arr[j] = arr[j - gap] # Ganti nilai arr[j] dengan nilai arr[j-gap]
                j -= gap # Kurangi nilai j dengan gap
                
            arr[j] = temp # Setelah loop selesai, set nilai arr[j] sama dengan nilai temp
        gap //= 2 # Bagi nilai gap dengan 2
        
    return arr # Kembalikan array yang telah diurutkan

# Penjelasan:

# Shell Sort adalah algoritma sorting yang menggunakan konsep Insertion Sort dengan mengurangi jumlah swap atau perpindahan data yang terjadi dalam proses sorting.
# Algoritma ini melakukan pengurutan dengan membagi array menjadi beberapa sub-array, kemudian melakukan pengurutan pada sub-array tersebut. Selama melakukan pengurutan, 
# Shell Sort akan mengurangi nilai gap yang digunakan untuk membagi array. Pada akhirnya, Shell Sort akan melakukan pengurutan pada seluruh data array dengan nilai gap = 1.

# def shell_sort(arr): : Membuat fungsi shell_sort dengan input array yang akan diurutkan.
# n = len(arr) : Mendapatkan panjang array.
# gap = n // 2 : Set nilai gap sebesar n/2.
# while gap > 0: : Selama nilai gap lebih besar dari 0, lakukan sorting.
# for i in range(gap, n): : Loop sebanyak gap hingga n.
# temp = arr[i] : Simpan nilai array pada index i pada variabel temp.
# j = i : Inisiasi variabel j sama dengan i.
# while j >= gap and arr[j - gap] > temp: : Selama nilai j lebih besar atau sama dengan gap dan nilai pada index arr[j-gap] lebih besar dari nilai temp, lakukan pengurutan secara Insertion Sort.
# arr[j] = arr[j - gap] : Ganti nilai arr[j] dengan nilai arr[j-gap].
# j -= gap : Kurangi nilai j dengan gap.
# arr[j] = temp : Setelah loop selesai, set nilai arr[j] sama dengan nilai temp.
# gap //= 2 : Bagi nilai gap dengan 2.
# return arr : Kembalikan array yang telah diurutkan.