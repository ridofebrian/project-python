import random

def main():
    angka_rahasia = random.randint(1, 50)
    percobaan = 0
    maks_percobaan = 7

    print("=== SELAMAT DATANG DI GAME TEBAK ANGKA ALA RWDOK ===")
    print("Aku memikirkan angka antara 1 sampai 50.")
    print(f"Kamu punya {maks_percobaan} kesempatan.\n")

    while percobaan < maks_percobaan:
        try:
            tebakan = int(input(f"Tebakan ke-{percobaan + 1}: "))
        except ValueError:
            print("Masukkan angka yang valid ya!")
            continue

        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil inimah bang\n")
        elif tebakan > angka_rahasia:
            print("kegedean bang\n")
        else:
            print(f"anjay benerrr Angkanya {angka_rahasia}. kamu nebak nya  {percobaan} kali.")
            return

    print(f"pokee pokee dah abis kesempatan mu. Angka yang benar adalah {angka_rahasia}.")

if __name__ == "__main__":
    main()