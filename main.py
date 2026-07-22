"""
🌸 Miyako AI
Version: 0.2

Author: Kadir
"""

def main():
    print("🌸 Miyako AI")
    print("Merhaba Kadir!")

    while True:
        komut = input("\nSen: ")

        if komut.lower() == "çık":
            print("Miyako: Görüşürüz!")
            break

        print(f"Miyako: '{komut}' dedin.")

if __name__ == "__main__":
    main()
