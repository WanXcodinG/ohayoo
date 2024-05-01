import subprocess
import time
import random

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def main():
    # Buka CMD
    execute_command("start cmd")

    execute_command("git add .")
    time.sleep(10)

    execute_command("git init")
    time.sleep(10)

    execute_command("git add README.md")
    time.sleep(10)

    execute_command('git commit -m "first commit"')
    time.sleep(10)

    execute_command("git branch -M main")
    time.sleep(10)

    execute_command("git remote add origin https://github.com/WanXcodinG/testingg.git")
    time.sleep(10)

    # Push ke branch utama
    execute_command("git push -u origin main")
    time.sleep(10)

    # Tunggu 10 detik
    time.sleep(10)

    # Tambahkan user npm
    execute_command("npm adduser")
    time.sleep(10)

    # Tunggu 10 detik
    time.sleep(20)

    # Publish npm
    execute_command("npm publish")

    # Tunggu 10 detik
    time.sleep(10)

    # Inisialisasi npm dengan scope
    execute_command("npm init --scope=@WanXcoinG")
    time.sleep(10)

    # Kirim kata-kata acak menggunakan fake
    random_message = "Ini adalah pesan acak: " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    print(random_message)

    # Delay 5 detik
    time.sleep(5)

    # Klik enter tujuh kali (saya asumsikan ini untuk menyetujui default)
    for _ in range(7):
        execute_command("echo. | npm publish")

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
