def menghitung_range():
    print("PROGRAM MENGHITUNG JUMLAH RANGE")
    x = input("masukan angka pertama :")
    x = int (x)
    input2=int(input('masukkan angka kedua :'))
    sum = 0
    for i in range(x, input2+1, 1):
        sum = sum+i
    print("Jumlah range adalah: ", sum )
menghitung_range()