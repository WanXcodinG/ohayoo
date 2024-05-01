import subprocess
import time
import random

def execute_command(command, input_text=None):
    try:
        if input_text is not None:
            proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
            proc.communicate(input_text.encode())
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def main():
    # Buka CMD
    execute_command("start cmd")

    execute_command("git add .")
    time.sleep(3)

    execute_command("git init")
    time.sleep(3)

    execute_command("git add README.md")
    time.sleep(3)

    execute_command('git commit -m "first commit"')
    time.sleep(10)

    execute_command("git branch -M main")
    time.sleep(10)

    execute_command("git remote add origin https://github.com/WanXcodinG/testingg.git")
    time.sleep(10)

    # Push ke branch utama
    execute_command("git push -u origin main")
    time.sleep(10)

    # Tambahkan user npm
    execute_command("npm adduser")

    # Tunggu 10 detik
    time.sleep(30)

    # Publish npm
    execute_command("npm publish")

    # Tunggu 10 detik
    time.sleep(10)

    # Inisialisasi npm dengan scope
    execute_command("npm init --scope=@WanXcoinG")

    # Tunggu 5 detik untuk memastikan inisialisasi selesai
    time.sleep(5)

    # Masukkan nama pengguna acak
    random_username = "fake_user_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    execute_command("", input_text=random_username + "\n")

    # Klik enter tujuh kali (saya asumsikan ini untuk menyetujui default)
    for _ in range(7):
        execute_command("", input_text="\n")

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
