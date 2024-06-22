import tkinter as tk
from tkinter import ttk

def on_activate_esp():
    if esp_var.get() == 1:
        print("ESP Activated")
        # -->Add code to activate ESP feature<--
    else:
        print("ESP Deactivated")
        # -->Add code to deactivate ESP feature<--

def on_activate_wallhack():
    if wallhack_var.get() == 1:
        print("Wallhack Activated")
        # -->Add code to activate Wallhack feature<--
    else:
        print("Wallhack Deactivated")
        # -->Add code to deactivate Wallhack feature<--

def on_activate_aimbot():
    if aimbot_var.get() == 1:
        print("Aimbot Activated")
        # -->Add code to activate Aimbot feature<--
    else:
        print("Aimbot Deactivated")
        # -->Add code to deactivate Aimbot feature<--

def on_activate_auto_trigger():
    if auto_trigger_var.get() == 1:
        print("Auto Trigger Activated")
        # -->Add code to activate Auto Trigger feature<--
    else:
        print("Auto Trigger Deactivated")
        # -->Add code to deactivate Auto Trigger feature<--

def on_fov_change(value):
    try:
        radius = float(value) / 10
        fov_label.config(text="FOV Radius: {:.1f}π".format(radius))
    except ValueError:
        pass

root = tk.Tk()
root.title("SPOOK 1.0")
root.geometry("480x220")

# window background
style = ttk.Style()
style.configure("TFrame", background="#c0c0c0", borderwidth=0, bordercolor="#c0c0c0", relief="flat")  # Blue-grayish fade background color

# Tab menu
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

# Settings tab
settings_tab = ttk.Frame(tab_control, style="TFrame")
tab_control.add(settings_tab, text="MAIN")

# ESP checkbox
esp_var = tk.IntVar()
esp_checkbox = ttk.Checkbutton(settings_tab, text="ESP", variable=esp_var, command=on_activate_esp, style="TCheckbutton")
esp_checkbox.pack()

# Wallhack checkbox
wallhack_var = tk.IntVar()
wallhack_checkbox = ttk.Checkbutton(settings_tab, text="Wallhack", variable=wallhack_var, command=on_activate_wallhack, style="TCheckbutton")
wallhack_checkbox.pack()

# Aimbot checkbox
aimbot_var = tk.IntVar()
aimbot_checkbox = ttk.Checkbutton(settings_tab, text="Aimbot", variable=aimbot_var, command=on_activate_aimbot, style="TCheckbutton")
aimbot_checkbox.pack()

# Auto Trigger checkbox
auto_trigger_var = tk.IntVar()
auto_trigger_checkbox = ttk.Checkbutton(settings_tab, text="Auto Trigger", variable=auto_trigger_var, command=on_activate_auto_trigger, style="TCheckbutton")
auto_trigger_checkbox.pack()

# FOV slider
fov_label = ttk.Label(settings_tab, text="FOV Radius: 0.0π")
fov_label.pack()
fov_slider = ttk.Scale(settings_tab, from_=0, to=100, orient="horizontal", command=on_fov_change, style="TScale")
fov_slider.pack()

# Radius entry
radius_label = ttk.Label(settings_tab, text="Radius")
radius_label.pack()
radius_entry = ttk.Entry(settings_tab)
radius_entry.pack()

while True:
    root.update()
