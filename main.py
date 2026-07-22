"""
🌸 Miyako AI
Version: 1.0

Author: Kadir
"""

from datetime import datetime
from memory import remember, recall
from ai import ask_ai

def main():
    print("🌸 Miyako AI")
    print("Merhaba Kadir! Ben Miyako.")
    print("Çıkmak için 'çık' yaz.\n")

    while True:
        komut = input("Sen: ").strip().lower()

        if komut == "çık":
            print("Miyako: Görüşürüz Kadir!")
            break

        elif komut == "yardım":
            print("""
Komutlar:
- yardım
- saat
- tarih
- benim adım ...
- benim adım ne
- çık
""")

        elif komut == "saat":
            print("Miyako:", datetime.now().strftime("%H:%M:%S"))

        elif komut == "tarih":
            print("Miyako:", datetime.now().strftime("%d.%m.%Y"))

        elif komut.startswith("benim adım "):
            isim = komut.replace("benim adım ", "")
            remember("isim", isim)
            print(f"Miyako: Memnun oldum {isim}. Seni unutmayacağım.")

        elif komut == "benim adım ne":
            isim = recall("isim")

            if isim:
                print(f"Miyako: Senin adın {isim}.")
            else:
                print("Miyako: Henüz adını söylemedin.")

        else:
            try:
                cevap = ask_ai(komut)
                print("Miyako:", cevap)

            except Exception as hata:
                print("Miyako: Yapay zekâya bağlanırken hata oluştu.")
                print(hata)


if __name__ == "__main__":
    main()
