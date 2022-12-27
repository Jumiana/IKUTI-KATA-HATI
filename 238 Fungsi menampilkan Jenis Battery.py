def jenis_baterai () :
    print("Jenis Batrai Yaitu:")

def baterai_primer () :
    print ("Batrai Zinc-Carbon, Batrai Alkaline, Batrai Lithium, Batrai Silver Oxide")
def baterai_sekunder ():
    print ("Batrai Ni-Cd, Batrai Ni-MH")

def jenisbaterai () :
    pilihan = int (input ("Masukkan pilihan:"))
    if pilihan == 1 :
        print (baterai_primer ())
        jenisbaterai ()
    elif pilihan == 2 :
        print (baterai_sekunder ())
        jenisbaterai ()
    else :
        print ("Masukkan anda salah")
        jenisbaterai ()

jenisbaterai ()