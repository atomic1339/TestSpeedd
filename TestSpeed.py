import speedtest
import sys
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet
import shutil

init(autoreset=True)

hari_mapping = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu"
}

def welcome_animation(text="WELCOME DI SCRIPT SAYA DASAR KAUM BEBAN ORTU!!", delay=0.1):
    for char in text:
        sys.stdout.write(Fore.CYAN + Style.BRIGHT + char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def banner():
    columns = shutil.get_terminal_size().columns
    ascii_banner = pyfiglet.figlet_format("SPEED TEST NETWORK", font="slant")
    banner_lines = ascii_banner.splitlines()
    print("=" * columns)
    for line in banner_lines:
        print(Fore.YELLOW + Style.BRIGHT + line.center(columns))
    right_text = "     script by-👹"
    print(" " * (columns - len(right_text)) + Fore.MAGENTA + Style.BRIGHT + right_text)
    print("=" * columns + "\n")

def spinner_loading(duration=5, message="Sabar Kontol"):
    spinner_chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        char = spinner_chars[i % len(spinner_chars)]
        sys.stdout.write(f'\r{message} {char}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')  # Clear line

def country_code_to_emoji(country_code):
    code_points = [ord(c) - ord('A') + 0x1F1E6 for c in country_code.upper()]
    return ''.join(chr(cp) for cp in code_points)

def cek_tipe_jaringan():
    try:
        res = requests.get('https://ipinfo.io/json', timeout=5)
        data = res.json()
        org = data.get('org','').lower()
        if '4g' in org:
            return "Jaringan yang digunakan: Jaringan Data Seluler 4G 📶"
        elif '3g' in org:
            return "Jaringan yang digunakan: Jaringan Data Seluler 3G 📶"
        elif any(k in org for k in ['5g']):
            return "Jaringan yang digunakan: Jaringan Data Seluler 5G 📶"
        elif any(k in org for k in ['mobile', 'cellular', 'telkomsel', 'xl', 'indosat']):
            return "Jaringan yang digunakan: Jaringan Data Seluler 📶"
        else:
            return "Jaringan yang digunakan: WiFi 📡"
    except:
        return "Tidak dapat mendeteksi jenis koneksi jaringan."

def get_public_ip_info():
    try:
        res = requests.get('https://ipinfo.io/json', timeout=5)
        data = res.json()
        ip = data.get('ip', 'Tidak diketahui')
        country = data.get('country', 'ID')
        return ip, country
    except:
        return "Tidak dapat mengambil IP publik.", "ID"

def cek_speed():
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "Sabar ya A.J.I.N.G lagi proses...\n")

    now = datetime.now()
    hari_eng = now.strftime("%A")
    hari_ind = hari_mapping.get(hari_eng, hari_eng)
    tanggal = now.strftime(f"{hari_ind}, %d %B %Y")
    ip, country_code = get_public_ip_info()
    flag = country_code_to_emoji(country_code)

    print(Fore.CYAN + f"Tanggal     : {tanggal}")
    print(Fore.CYAN + f"Negara     : {country_code} {flag}")
    print(Fore.CYAN + f"IP publik  : {ip}")
    print(Fore.CYAN + cek_tipe_jaringan() + "\n")

    st = speedtest.Speedtest(secure=True)
    print(Fore.CYAN + "Mengambil server terbaik...")
    st.get_best_server()

    print(Fore.CYAN + "Mulai pengujian download...")
    spinner_loading(duration=5, message="Download")

    download = st.download() / 1_000_000

    print(Fore.CYAN + "Mulai pengujian upload...")
    spinner_loading(duration=5, message="Upload")

    upload = st.upload() / 1_000_000

    ping = st.results.ping
    print(f"{Fore.GREEN}Download Speed: {download:.2f} Mbps")
    print(f"{Fore.GREEN}Upload Speed: {upload:.2f} Mbps")
    print(f"{Fore.GREEN}Ping: {ping:.2f} ms\n")
    if ping < 50 and download > 10 and upload > 5:
        print(Fore.GREEN + Style.BRIGHT + "Koneksi bagus untuk bermain game online.")
    else:
        print(Fore.RED + Style.BRIGHT + "Koneksi kurang ideal untuk bermain game online.")
    print("\n" + Fore.MAGENTA + Style.BRIGHT + "Check speed done K.O.N.T.O.L 🖕.")

def main_menu():
    welcome_animation()
    banner()
    while True:
        print("Pilih yang Di bawah ini KONTOL 👇👇")
        print("1. Testspeed")
        print("2. Exit")
        pilihan = input("Masukkan pilihan (1/2): ").strip()
        if pilihan == '1':
            cek_speed()
        elif pilihan == '2':
            print(Fore.RED + Style.BRIGHT + "SelamaT Tinggal Jangan Datang Lagi ya .K.O.N.T.O.L.!!!👹🤬")
            sys.exit(0)
        else:
            print(Fore.YELLOW + "Pilihan tidak valid, silahkan coba lagi.\n")

if __name__ == "__main__":
    main_menu()
