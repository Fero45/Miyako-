"""
🌸 Miyako AI
Version: 0.3

Author: Kadir
"""

from datetime import datetime

def main():
    print("🌸 Miyako AI")
    print("Merhaba Kadir!")

    while True:
        komut = input("\nSen: ").lower()

        if komut == "çık":
            print("Miyako: Görüşürüz!")
            break

        elif komut == "yardım":
            print("""
Komutlar:
- yardım
- saat
- tarih
- çık
""")

        elif komut == "saat":
            print("Miyako:", datetime.now().strftime("%H:%M:%S"))

        elif komut == "tarih":
            print("Miyako:", datetime.now().strftime("%d.%m.%Y"))

        else:
            print(f"Miyako: '{komut}' dedin.")

if __name__ == "__main__":
    main()
