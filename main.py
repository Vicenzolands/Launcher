import subprocess
import os
import customtkinter as ctk

print("Testando Launcher")

def study():
    subprocess.Popen(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    subprocess.Popen(r"C:\Users\vicen\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    subprocess.Popen(r"wt.exe")

def play():
    subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")
    subprocess.Popen(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    subprocess.Popen([r"C:\Users\vicen\AppData\Local\Discord\Update.exe", "--processStart", "Discord.exe"])
    os.startfile("whatsapp:")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.title("Launcher")
window.geometry("300x150")

button_study = ctk.CTkButton(window, text="📚 Estudo", command=study, width=200, height=50, font=("Arial", 16))
button_study.pack(pady=10)
button_play = ctk.CTkButton(window, text="🎮 Jogos", command=play, width=200, height=50, font=("Arial", 16))
button_play.pack(pady=10)

window.mainloop()
