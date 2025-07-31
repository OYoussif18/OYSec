import customtkinter as ctk
import os
import sys

# Add core folder to sys.path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import custom modules from core
from core.privesc import *
from core.recon import *
from core.utils import *

# --------------------------- #
# Setup App Appearance & Theme
# --------------------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
default_color = "#bb0000"
hover_color = "#550000"

# --------------------------- #
# Create Main Application Window
# --------------------------- #
app = ctk.CTk()
app.geometry("400x300")
app.title("OYSec")

# Set icon
icon_path = os.path.join(os.path.dirname(__file__), "../assets/icon.png")
app.iconbitmap(icon_path)

# --------------------------- #
# Define Pages/Frames
# --------------------------- #
home_frame = ctk.CTkFrame(app)
recon_frame = ctk.CTkScrollableFrame(app)
fast_nmap_page = ctk.CTkFrame(app) 
full_nmap_page = ctk.CTkFrame(app)
gobuster_page = ctk.CTkFrame(app)
http_headers_page = ctk.CTkFrame(app)
run_command_page = ctk.CTkFrame(app)
privesc_frame = ctk.CTkFrame(app)
utils_frame = ctk.CTkFrame(app)

# --------------------------- #
# Navigation: Frame Switching Function
# --------------------------- #
def show_frame(frame):
    # Hide all pages first
    home_frame.pack_forget()
    recon_frame.pack_forget()
    privesc_frame.pack_forget()
    utils_frame.pack_forget()
    fast_nmap_page.pack_forget()
    full_nmap_page.pack_forget()
    gobuster_page.pack_forget()
    http_headers_page.pack_forget()
    run_command_page.pack_forget()
    # Show the requested frame
    frame.pack(fill="both", expand=True)

# --------------------------- #
# Home Page Content
# --------------------------- #
hello_label = ctk.CTkLabel(home_frame, text="Welcome to OYSec", font=("Arial", 24))
hello_label.pack(pady=20)

# Navigation Buttons on Home Page
recon_button = ctk.CTkButton(home_frame, text="Recon", command=lambda: show_frame(recon_frame), fg_color=default_color, hover_color=hover_color)
recon_button.pack(pady=10)

privesc_button = ctk.CTkButton(home_frame, text="Privesc", command=lambda: show_frame(privesc_frame), fg_color=default_color, hover_color=hover_color)
privesc_button.pack(pady=10)

utils_button = ctk.CTkButton(home_frame, text="Utils", command=lambda: show_frame(utils_frame), fg_color=default_color, hover_color=hover_color)
utils_button.pack(pady=10)

# --------------------------- #
# Recon Page
# --------------------------- #

# Back button on top to return to home
back_button_recon = ctk.CTkButton(recon_frame, text="Back to Home", command=lambda: show_frame(home_frame), fg_color=default_color, hover_color=hover_color)
back_button_recon.pack(pady=10)


# ---- Fast Nmap Tool Section ----
fast_nmap_section = ctk.CTkFrame(recon_frame)
fast_nmap_section.pack(pady=10, fill="x")

# Function to run Fast Nmap
def run_fast_nmap():
    target = fast_nmap_entry.get()
    if target:
        output = fast_nmap(target)
        terminal_fast_nmap_output.configure(text=output)
    else:
        terminal_fast_nmap_output.configure(text="Please enter a target.")

# Button to open Fast Nmap tool page
fast_nmap_button_page_button = ctk.CTkButton(
    fast_nmap_section,
    text="Fast Nmap",
    command=lambda: show_frame(fast_nmap_page),
    fg_color=default_color,
    hover_color=hover_color
)
fast_nmap_button_page_button.pack(pady=5)

# Fast Nmap Page UI
ctk.CTkButton(
    fast_nmap_page,
    text="Back to Recon",
    command=lambda: show_frame(recon_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(fast_nmap_page, text="Fast Nmap Scan").pack(pady=5)

fast_nmap_entry = ctk.CTkEntry(fast_nmap_page, placeholder_text="Enter target")
fast_nmap_entry.pack(pady=5, padx=10, fill="x")

fast_nmap_button = ctk.CTkButton(
    fast_nmap_page,
    text="Run",
    command=run_fast_nmap,
    fg_color=default_color,
    hover_color=hover_color
)
fast_nmap_button.pack(pady=5)

terminal_fast_nmap_output = ctk.CTkLabel(
    fast_nmap_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_fast_nmap_output.pack(pady=5, padx=10, fill="both", expand=True)


# ---- Full Nmap Tool Section ----
full_nmap_section = ctk.CTkFrame(recon_frame)
full_nmap_section.pack(pady=10, fill="x")

# Button to open Full Nmap tool page
full_nmap_button_page_button = ctk.CTkButton(
    full_nmap_section,
    text="Full Nmap",
    command=lambda: show_frame(full_nmap_page),
    fg_color=default_color,
    hover_color=hover_color
)
full_nmap_button_page_button.pack(pady=5)

# Function to run Full Nmap
def run_full_nmap():
    target = full_nmap_entry.get()
    if target:
        output = full_nmap(target)
        terminal_full_nmap_output.configure(text=output)
    else:
        terminal_full_nmap_output.configure(text="Please enter a target.")

# Full Nmap Page UI
ctk.CTkButton(
    full_nmap_page,
    text="Back to Recon",
    command=lambda: show_frame(recon_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(full_nmap_page, text="Full Nmap Scan").pack(pady=5)

full_nmap_entry = ctk.CTkEntry(full_nmap_page, placeholder_text="Enter target")
full_nmap_entry.pack(pady=5, padx=10, fill="x")

full_nmap_button = ctk.CTkButton(
    full_nmap_page,
    text="Run",
    command=run_full_nmap,
    fg_color=default_color,
    hover_color=hover_color
)
full_nmap_button.pack(pady=5)

terminal_full_nmap_output = ctk.CTkLabel(
    full_nmap_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_full_nmap_output.pack(pady=5, padx=10, fill="both", expand=True)



# ---- Gobuster Directory Tool Section ----
gobuster_section = ctk.CTkFrame(recon_frame)
gobuster_section.pack(pady=10, fill="x")

# Button to open Gobuster Directory tool page
gobuster_button_page_button = ctk.CTkButton(
    gobuster_section,
    text="Gobuster Directory",
    command=lambda: show_frame(gobuster_page),
    fg_color=default_color,
    hover_color=hover_color
)
gobuster_button_page_button.pack(pady=5)

# Function to run Gobuster Directory
def run_gobuster():
    target = gobuster_target_entry.get()
    wordlist = gobuster_wordlist_entry.get()
    if target and wordlist:
        output = gobuster_directory(target, wordlist)
        terminal_gobuster_output.configure(text=output)
    else:
        terminal_gobuster_output.configure(text="Please enter both target and wordlist path.")

# Gobuster Directory Page UI
ctk.CTkButton(
    gobuster_page,
    text="Back to Recon",
    command=lambda: show_frame(recon_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(gobuster_page, text="Gobuster Directory Scan").pack(pady=5)

gobuster_target_entry = ctk.CTkEntry(gobuster_page, placeholder_text="Enter target")
gobuster_target_entry.pack(pady=5, padx=10, fill="x")

gobuster_wordlist_entry = ctk.CTkEntry(gobuster_page, placeholder_text="Enter wordlist path")
gobuster_wordlist_entry.pack(pady=5, padx=10, fill="x")

gobuster_button = ctk.CTkButton(
    gobuster_page,
    text="Run",
    command=run_gobuster,
    fg_color=default_color,
    hover_color=hover_color
)
gobuster_button.pack(pady=5)

terminal_gobuster_output = ctk.CTkLabel(
    gobuster_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_gobuster_output.pack(pady=5, padx=10, fill="both", expand=True)


# ---- HTTP Enum Tool Section ----
http_enum_section = ctk.CTkFrame(recon_frame)
http_enum_section.pack(pady=10, fill="x")

def run_http_enum():
    target = http_enum_entry.get()
    if target:
        output = http_headers(target)
        terminal_http_enum_output.configure(text=output)
    else:
        terminal_http_enum_output.configure(text="Please enter a target.")

http_enum_button_page_button = ctk.CTkButton(
    http_enum_section,
    text="HTTP Enum",
    command=lambda: show_frame(http_headers_page),
    fg_color=default_color,
    hover_color=hover_color
)
http_enum_button_page_button.pack(pady=5)

ctk.CTkButton(
    http_headers_page,
    text="Back to Recon",
    command=lambda: show_frame(recon_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(http_headers_page, text="HTTP Enumeration").pack(pady=5)

http_enum_entry = ctk.CTkEntry(http_headers_page, placeholder_text="Enter target")
http_enum_entry.pack(pady=5, padx=10, fill="x")

http_enum_button = ctk.CTkButton(
    http_headers_page,
    text="Run",
    command=run_http_enum,
    fg_color=default_color,
    hover_color=hover_color
)
http_enum_button.pack(pady=5)

terminal_http_enum_output = ctk.CTkLabel(
    http_headers_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_http_enum_output.pack(pady=5, padx=10, fill="both", expand=True)


# ---- Run Command Tool Section ----
run_command_section = ctk.CTkFrame(recon_frame)
run_command_section.pack(pady=10, fill="x")

def run_custom_command():
    cmd = run_command_entry.get()
    if cmd:
        output = run_command(cmd)
        terminal_run_command_output.configure(text=output)
    else:
        terminal_run_command_output.configure(text="Please enter a command.")

run_command_button_page_button = ctk.CTkButton(
    run_command_section,
    text="Run Command",
    command=lambda: show_frame(run_command_page),
    fg_color=default_color,
    hover_color=hover_color
)
run_command_button_page_button.pack(pady=5)

ctk.CTkButton(
    run_command_page,
    text="Back to Recon",
    command=lambda: show_frame(recon_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(run_command_page, text="Run Shell Command").pack(pady=5)

run_command_entry = ctk.CTkEntry(run_command_page, placeholder_text="Enter command")
run_command_entry.pack(pady=5, padx=10, fill="x")

run_command_button = ctk.CTkButton(
    run_command_page,
    text="Run",
    command=run_custom_command,
    fg_color=default_color,
    hover_color=hover_color
)
run_command_button.pack(pady=5)

terminal_run_command_output = ctk.CTkLabel(
    run_command_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_run_command_output.pack(pady=5, padx=10, fill="both", expand=True)


# --------------------------- #
# Privesc Page - Placeholder for now
# --------------------------- #

# --------------------------- #
# Utils Page - Placeholder for now
# --------------------------- #

# --------------------------- #
# Start on Home Page
# --------------------------- #
home_frame.pack(fill="both", expand=True)
app.mainloop()
