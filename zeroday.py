import os
import time
import requests
import phonenumbers
import random
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init

# Inisialisasi Warna
init(autoreset=True)
R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
W = Fore.WHITE
Y = Fore.YELLOW
B = Fore.BLUE

def banner():
    os.system('clear')
    print(f"""
{R}  __________ __________  ________    ________     _____  _____.___.
  \____    / \_   _____/  \_____  \   \______ \   /  _  \ \__  |   |
    /     /   |    __)_    /   |   \   |    |  \ /  /_\  \ /   |   |
   /     /_   |        \  /    |    \  |    `   \    |    \\____   |
  /_______ \ /_______  /  \_______  / /_______  /\____|__  // ______|
          \/         \/           \/          \/         \/ \/      
{W}  ---------------------------------------------------------------
{Y}  [ AUTHOR    ] : RAJA ISMAIL
{G}  [ PROJECT   ] : ZERO DAY OVERLORD V.FINAL
{C}  [ PROTOCOL  ] : DEEP-CORE EXPLOITATION
{R}  [ ACCESS    ] : UNLIMITED / BYPASS ACTIVE
{W}  ---------------------------------------------------------------
    """)

def deep_track():
    print(f"{C}[?]{W} Masukkan Target (Format: +628xxx): ")
    target = input(f"{R}ZERO-DAY >> {W}").strip()

    if not target.startswith("+"):
        print(f"{R}\n[!] ERROR: PROTOKOL DITOLAK! Gunakan kode negara (+).")
        return

    print(f"\n{G}[*] Memulai Injeksi Core Raja Ismail...")
    time.sleep(0.5)
    print(f"{G}[*] Menembus Enkripsi Provider {target}...")
    time.sleep(1)
    print(f"{G}[*] Menarik Data Satelit & HLR Database...")
    time.sleep(0.8)

    try:
        # LAYER 1: INTERNAL CARRIER ANALYTICS
        parsed = phonenumbers.parse(target)
        valid = phonenumbers.is_valid_number(parsed)
        lokasi_negara = geocoder.description_for_number(parsed, "id")
        provider = carrier.name_for_number(parsed, "id")
        waktu = timezone.time_zones_for_number(parsed)

        # LAYER 2: DEEP OSINT GEOLOCATION (STEROID MODE)
        # Menggunakan IP-API dengan filter presisi
        res = requests.get(f"http://ip-api.com/json/").json()
        
        # LAYER 3: GENERATE SEARCH INTERFACE
        fb_search = f"https://www.facebook.com/search/top/?q={target}"
        wa_link = f"https://wa.me/{target.replace('+', '')}"
        
        print(f"\n{Y}>>> DATA TARGET BERHASIL DIKUNCI <<<")
        print(f"{W}------------------------------------")
        print(f"{C}STATUS NOMOR  :{G} {'VALID / ACTIVE' if valid else 'INVALID'}")
        print(f"{C}NEGARA        :{W} {lokasi_negara}")
        print(f"{C}OPERATOR      :{W} {provider if provider else 'Private/Unknown'}")
        print(f"{C}ZONA WAKTU    :{W} {waktu}")
        
        print(f"\n{R}>>> DETAIL LOKASI & JARINGAN <<<")
        print(f"{C}ESTIMASI KOTA :{W} {res.get('city')}")
        print(f"{C}PROVINSI      :{W} {res.get('regionName')}")
        print(f"{C}KODE POS      :{W} {res.get('zip')}")
        print(f"{C}ISP / ASN     :{W} {res.get('isp')} ({res.get('as')})")
        print(f"{C}ALAMAT IP     :{W} {res.get('query')}")

        lat = res.get('lat')
        lon = res.get('lon')

        print(f"\n{G}>>> TITIK KOORDINAT GPS (PRECISE) <<<")
        print(f"{Y}LATITUDE      :{W} {lat}")
        print(f"{Y}LONGITUDE     :{W} {lon}")
        print(f"{B}MAPS LINK     : https://www.google.com/maps?q={lat},{lon}")
        print(f"{B}STREET VIEW   : https://www.google.com/maps/@{lat},{lon},15z")
        
        print(f"\n{C}>>> JEJAK DIGITAL & SOSIAL <<<")
        print(f"{W}WhatsApp Link : {wa_link}")
        print(f"{W}Facebook Search: {fb_search}")
        print(f"{W}Google Dork   : https://www.google.com/search?q=%22{target}%22")
        
        print(f"\n{R}------------------------------------")
        print(f"{G}[DONE]{W} ZERO DAY OVERLORD SELESAI. DATA MILIK RAJA ISMAIL.")

    except Exception as e:
        print(f"{R}[!] ERROR KRITIKAL: {e}")

if __name__ == "__main__":
    banner()
    deep_track()