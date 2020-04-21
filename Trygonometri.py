def SIN(A,B):
    return A/B

def COS(A,B):
    return A/B

def TAN(A,B):
    return A/B

print("ATURAN TRYGONOMETRI")
while True :
    print("Menu pilihan:\n")
    print("1. SIN\n")
    print("2. COS\n")
    print("3. TAN\n")
    
    pilih=int(input("Masukkan pilihan :"))

    if pilih==1:
        A=int(input("Masukkan Depan:"))
        B=int(input("Masukkan Miring:"))
        print("hasil dari SIN adalah {}".format(SIN(A,B)))
    elif pilih==2:
        A=int(input("Masukkan Samping:"))
        B=int(input("Masukkan Miring:"))
        print("hasil dari COS adalah {}".format(COS(A,B)))
    elif pilih==3:
        A=int(input("Masukkan Depan:"))
        B=int(input("Masukkan Samping:"))
        print("hasil dari TAN adalah {}".format(TAN(A,B)))
    else :
        print("pilihan tidak ada")
    

