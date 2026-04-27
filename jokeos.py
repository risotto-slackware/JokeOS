import tkinter as tk
import random

# --- joke logs ---

linux_jokes = [
    "[OK] init: user privilege escalation detected (sudo dependency required)",
    "[KERNEL] panic avoided: user tried to exit vim without saving again",
    "[ERROR] /dev/happiness not found. Recompiling emotions... FAILED",
    "[SYSTEM] compiling life.c ... warning: infinite loop of poor decisions detected",
    "[SERVICE] systemd: restarting motivation.service (failed: dependency missing 'sleep')"
]

windows_jokes = [
    "[ERROR 0x0000FEEL] Windows Update is configuring disappointment (42%)",
    "[TASKMGR] 98% CPU used by 'nothing important.exe'",
    "[SYSTEM] Blue Screen of Happiness initiated... rebooting sadness driver",
    "[UPDATE] Installing update 1 of 1: 'fixing things that weren't broken'",
    "[SECURITY] Defender blocked user from doing anything useful"
]

mac_jokes = [
    "[APPLE] Optimizing system by removing features you liked",
    "[iOS] AirDrop detected emotions. Blocking transfer for privacy",
    "[SYSTEM] Port detected. Removing for aesthetic reasons",
    "[iCloud] Sync failed: storage full (upgrade to buy more sadness)",
    "[SECURITY] User attempted freedom. System Integrity Protection activated"
]

# --- GUI logic ---

def show_boot(os_name):
    label.config(text=f"[BOOT] Initializing {os_name} subsystem...\nPlease wait...")
    root.after(1000, lambda: show_joke(os_name))


def show_joke(os_name):
    if os_name == "Linux":
        joke = random.choice(linux_jokes)
    elif os_name == "Windows":
        joke = random.choice(windows_jokes)
    else:
        joke = random.choice(mac_jokes)

    label.config(text=joke)


# --- GUI setup ---

root = tk.Tk()
root.title("JokeOS Terminal Simulator")
root.geometry("520x300")
root.configure(bg="black")

label = tk.Label(
    root,
    text="Select a system to initialize",
    fg="lime",
    bg="black",
    font=("Courier", 11),
    wraplength=480,
    justify="left"
)
label.pack(pady=30)

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

tk.Button(
    btn_frame,
    text="Boot Linux 🐧",
    command=lambda: show_boot("Linux"),
    fg="black"
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame,
    text="Boot Windows 🪟",
    command=lambda: show_boot("Windows"),
    fg="black"
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame,
    text="Boot Mac 🍎",
    command=lambda: show_boot("Mac"),
    fg="black"
).grid(row=0, column=2, padx=5)

root.mainloop()
