import customtkinter as ctk
import os
import sys
import pyperclip

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
# recon frames
fast_nmap_page = ctk.CTkFrame(app) 
full_nmap_page = ctk.CTkFrame(app)
gobuster_page = ctk.CTkFrame(app)
http_headers_page = ctk.CTkFrame(app)
run_command_page = ctk.CTkFrame(app)
#____________________________________
privesc_frame = ctk.CTkScrollableFrame(app)
#privesc frames
reverse_shell_listener_page = ctk.CTkFrame(app)
check_sudo_permissions_page = ctk.CTkFrame(app)
find_suid_binaries_page = ctk.CTkFrame(app)
get_kernel_version_page = ctk.CTkFrame(app)
find_writable_files_page = ctk.CTkFrame(app)
check_cron_jobs_page = ctk.CTkFrame(app)
search_for_credentials_page = ctk.CTkFrame(app)
#____________________________________
utils_frame = ctk.CTkScrollableFrame(app)
# utils frames
encode_base64_page = ctk.CTkFrame(app)
decode_base64_page = ctk.CTkFrame(app)
url_encode_page = ctk.CTkFrame(app)
url_decode_page = ctk.CTkFrame(app)
random_user_agent_page = ctk.CTkFrame(app)
decode_jwt_page = ctk.CTkFrame(app)
generate_uuid_page = ctk.CTkFrame(app)
#_____________________________________


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
    reverse_shell_listener_page.pack_forget()
    check_sudo_permissions_page.pack_forget()
    find_suid_binaries_page.pack_forget()
    get_kernel_version_page.pack_forget()
    find_writable_files_page.pack_forget()
    check_cron_jobs_page.pack_forget()
    search_for_credentials_page.pack_forget()
    encode_base64_page.pack_forget()
    decode_base64_page.pack_forget()
    url_encode_page.pack_forget()
    url_decode_page.pack_forget()
    random_user_agent_page.pack_forget()
    decode_jwt_page.pack_forget()
    generate_uuid_page.pack_forget()
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
# Privesc Page
# --------------------------- #
 
 # Back button on top to return to home
back_button_privesc = ctk.CTkButton(privesc_frame, text="Back to Home", command=lambda: show_frame(home_frame), fg_color=default_color, hover_color=hover_color)
back_button_privesc.pack(pady=10)

# ---- Reverse Shell Listener Section ----
reverse_shell_listener_section = ctk.CTkFrame(privesc_frame)
reverse_shell_listener_section.pack(pady=10, fill="x")

reverse_shell_listener_button_page_button = ctk.CTkButton(
    reverse_shell_listener_section,
    text="Reverse Shell Listener",
    command=lambda: show_frame(reverse_shell_listener_page),
    fg_color=default_color,
    hover_color=hover_color
)
reverse_shell_listener_button_page_button.pack(pady=5)

# UI for Reverse Shell Listener Page
ctk.CTkButton(
    reverse_shell_listener_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(reverse_shell_listener_page, text="Reverse Shell Listener").pack(pady=5)

reverse_shell_port_entry = ctk.CTkEntry(reverse_shell_listener_page, placeholder_text="Enter port")
reverse_shell_port_entry.pack(pady=5, padx=10, fill="x")

# Function to run Reverse Shell Listener
def run_reverse_shell_listener():
    port = reverse_shell_port_entry.get()
    if port:
        
        reverse_shell_listener(port)
        terminal_reverse_shell_output.configure(text=f"Listening on port {port}...")
    else:
        terminal_reverse_shell_output.configure(text="Please enter a port.")

reverse_shell_listener_button = ctk.CTkButton(
    reverse_shell_listener_page,
    text="Start Listener",
    command=run_reverse_shell_listener,
    fg_color=default_color,
    hover_color=hover_color
)
reverse_shell_listener_button.pack(pady=5)

terminal_reverse_shell_output = ctk.CTkLabel(
    reverse_shell_listener_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_reverse_shell_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Check Sudo Permissions Section ----
check_sudo_permissions_section = ctk.CTkFrame(privesc_frame)
check_sudo_permissions_section.pack(pady=10, fill="x")

check_sudo_permissions_button_page_button = ctk.CTkButton(
    check_sudo_permissions_section,
    text="Check Sudo Permissions",
    command=lambda: show_frame(check_sudo_permissions_page),
    fg_color=default_color,
    hover_color=hover_color
)
check_sudo_permissions_button_page_button.pack(pady=5)

# UI for Check Sudo Permissions Page
ctk.CTkButton(
    check_sudo_permissions_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(check_sudo_permissions_page, text="Check Sudo Permissions").pack(pady=5)

def run_check_sudo_permissions():
    output = check_sudo_permissions()
    terminal_check_sudo_output.configure(text=output)
    pyperclip.copy("sudo -l")


check_sudo_permissions_button = ctk.CTkButton(
    check_sudo_permissions_page,
    text="Copy Command",
    command=run_check_sudo_permissions,
    fg_color=default_color,
    hover_color=hover_color
)
check_sudo_permissions_button.pack(pady=5)

terminal_check_sudo_output = ctk.CTkLabel(
    check_sudo_permissions_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_check_sudo_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Find SUID Binaries Section ----
find_suid_binaries_section = ctk.CTkFrame(privesc_frame)
find_suid_binaries_section.pack(pady=10, fill="x")

find_suid_binaries_button_page_button = ctk.CTkButton(
    find_suid_binaries_section,
    text="Find SUID Binaries",
    command=lambda: show_frame(find_suid_binaries_page),
    fg_color=default_color,
    hover_color=hover_color
)
find_suid_binaries_button_page_button.pack(pady=5)

# UI for Find SUID Binaries Page
ctk.CTkButton(
    find_suid_binaries_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(find_suid_binaries_page, text="Find SUID Binaries").pack(pady=5)
def run_find_suid_binaries():
    output = find_suid_binaries()
    terminal_find_suid_output.configure(text=output)
    pyperclip.copy("find / -perm -4000 -type f 2>/dev/null")

find_suid_binaries_button = ctk.CTkButton(
    find_suid_binaries_page,
    text="Copy Command",
    command=run_find_suid_binaries,
    fg_color=default_color,
    hover_color=hover_color
)
find_suid_binaries_button.pack(pady=5)

terminal_find_suid_output = ctk.CTkLabel(
    find_suid_binaries_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_find_suid_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Get Kernel Version Section ----
get_kernel_version_section = ctk.CTkFrame(privesc_frame)
get_kernel_version_section.pack(pady=10, fill="x")

get_kernel_version_button_page_button = ctk.CTkButton(
    get_kernel_version_section,
    text="Get Kernel Version",
    command=lambda: show_frame(get_kernel_version_page),
    fg_color=default_color,
    hover_color=hover_color
)
get_kernel_version_button_page_button.pack(pady=5)

# UI for Get Kernel Version Page
ctk.CTkButton(
    get_kernel_version_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(get_kernel_version_page, text="Get Kernel Version").pack(pady=5)
def run_get_kernel_version():
    output = get_kernel_version()
    terminal_get_kernel_output.configure(text=output)
    pyperclip.copy("uname -r")
get_kernel_version_button = ctk.CTkButton(
    get_kernel_version_page,
    text="Copy Command",
    command=run_get_kernel_version,
    fg_color=default_color,
    hover_color=hover_color
)
get_kernel_version_button.pack(pady=5)

terminal_get_kernel_output = ctk.CTkLabel(
    get_kernel_version_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_get_kernel_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Find Writable Files Section ----
find_writable_files_section = ctk.CTkFrame(privesc_frame)
find_writable_files_section.pack(pady=10, fill="x")

find_writable_files_button_page_button = ctk.CTkButton(
    find_writable_files_section,
    text="Find Writable Files",
    command=lambda: show_frame(find_writable_files_page),
    fg_color=default_color,
    hover_color=hover_color
)
find_writable_files_button_page_button.pack(pady=5)

# UI for Find Writable Files Page
ctk.CTkButton(
    find_writable_files_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(find_writable_files_page, text="Find Writable Files").pack(pady=5)
def run_find_writable_files():
    output = find_writable_files()
    terminal_find_writable_output.configure(text=output)
    pyperclip.copy("find / -writable -type f 2>/dev/null")
find_writable_files_button = ctk.CTkButton(
    find_writable_files_page,
    text="Copy Command",
    command=run_find_writable_files,
    fg_color=default_color,
    hover_color=hover_color
)
find_writable_files_button.pack(pady=5)

terminal_find_writable_output = ctk.CTkLabel(
    find_writable_files_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_find_writable_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Check Cron Jobs Section ----
check_cron_jobs_section = ctk.CTkFrame(privesc_frame)
check_cron_jobs_section.pack(pady=10, fill="x")

check_cron_jobs_button_page_button = ctk.CTkButton(
    check_cron_jobs_section,
    text="Check Cron Jobs",
    command=lambda: show_frame(check_cron_jobs_page),
    fg_color=default_color,
    hover_color=hover_color
)
check_cron_jobs_button_page_button.pack(pady=5)

# UI for Check Cron Jobs Page
ctk.CTkButton(
    check_cron_jobs_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(check_cron_jobs_page, text="Check Cron Jobs").pack(pady=5)
def run_check_cron_jobs():
    output = check_cron_jobs()
    terminal_check_cron_output.configure(text=output)
    pyperclip.copy("cat /etc/crontab; ls -l /etc/cron*")
check_cron_jobs_button = ctk.CTkButton(
    check_cron_jobs_page,
    text="Copy Command",
    command=run_check_cron_jobs,
    fg_color=default_color,
    hover_color=hover_color
)
check_cron_jobs_button.pack(pady=5)

terminal_check_cron_output = ctk.CTkLabel(
    check_cron_jobs_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_check_cron_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Search for Credentials Section ----
search_for_credentials_section = ctk.CTkFrame(privesc_frame)
search_for_credentials_section.pack(pady=10, fill="x")

search_for_credentials_button_page_button = ctk.CTkButton(
    search_for_credentials_section,
    text="Search for Credentials",
    command=lambda: show_frame(search_for_credentials_page),
    fg_color=default_color,
    hover_color=hover_color
)
search_for_credentials_button_page_button.pack(pady=5)

# UI for Search for Credentials Page
ctk.CTkButton(
    search_for_credentials_page,
    text="Back to Privesc",
    command=lambda: show_frame(privesc_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(search_for_credentials_page, text="Search for Credentials").pack(pady=5)
def run_search_for_credentials():
    output = search_for_credentials()
    terminal_search_credentials_output.configure(text=output)
    pyperclip.copy("grep -ri 'password\\|passwd\\|secret\\|key' /home 2>/dev/null")
search_for_credentials_button = ctk.CTkButton(
    search_for_credentials_page,
    text="Copy Command",
    command=run_search_for_credentials,
    fg_color=default_color,
    hover_color=hover_color
)
search_for_credentials_button.pack(pady=5)

terminal_search_credentials_output = ctk.CTkLabel(
    search_for_credentials_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_search_credentials_output.pack(pady=5, padx=10, fill="both", expand=True)

# --------------------------- #
# Utils Page
# --------------------------- #

# Back button on top to return to home
back_button_utils = ctk.CTkButton(utils_frame, text="Back to Home", command=lambda: show_frame(home_frame), fg_color=default_color, hover_color=hover_color)
back_button_utils.pack(pady=10)

# ---- Encode Base64 Section ----
encode_base64_section = ctk.CTkFrame(utils_frame)
encode_base64_section.pack(pady=10, fill="x")

def run_encode_base64():
    text = encode_base64_entry.get()
    if text:
        output = encode_base64(text)
        terminal_encode_base64_output.configure(text=output)
        pyperclip.copy(output)
    else:
        terminal_encode_base64_output.configure(text="Please enter text to encode.")
encode_base64_button_page_button = ctk.CTkButton(
    encode_base64_section,
    text="Encode Base64",
    command=lambda: show_frame(encode_base64_page),
    fg_color=default_color,
    hover_color=hover_color
)
encode_base64_button_page_button.pack(pady=5)

# UI for Encode Base64 Page
ctk.CTkButton(
    encode_base64_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(encode_base64_page, text="Encode to Base64").pack(pady=5)

encode_base64_entry = ctk.CTkEntry(encode_base64_page, placeholder_text="Enter text to encode")
encode_base64_entry.pack(pady=5, padx=10, fill="x")
encode_base64_button = ctk.CTkButton(
    encode_base64_page,
    text="Encode",
    command=run_encode_base64,
    fg_color=default_color,
    hover_color=hover_color
)
encode_base64_button.pack(pady=5)

terminal_encode_base64_output = ctk.CTkLabel(
    encode_base64_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_encode_base64_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Decode Base64 Section ----
decode_base64_section = ctk.CTkFrame(utils_frame)
decode_base64_section.pack(pady=10, fill="x")

def run_decode_base64():
    text = decode_base64_entry.get()
    if text:
        output = decode_base64(text)
        terminal_decode_base64_output.configure(text=output)
        pyperclip.copy(output)
    else:
        terminal_decode_base64_output.configure(text="Please enter text to decode.")
decode_base64_button_page_button = ctk.CTkButton(
    decode_base64_section,
    text="Decode Base64",
    command=lambda: show_frame(decode_base64_page),
    fg_color=default_color,
    hover_color=hover_color
)
decode_base64_button_page_button.pack(pady=5)

# UI for Decode Base64 Page
ctk.CTkButton(
    decode_base64_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(decode_base64_page, text="Decode from Base64").pack(pady=5)

decode_base64_entry = ctk.CTkEntry(decode_base64_page, placeholder_text="Enter Base64 text to decode")

decode_base64_entry.pack(pady=5, padx=10, fill="x")
decode_base64_button = ctk.CTkButton(
    decode_base64_page,
    text="Decode",
    command=run_decode_base64,
    fg_color=default_color,
    hover_color=hover_color
)
decode_base64_button.pack(pady=5)

terminal_decode_base64_output = ctk.CTkLabel(
    decode_base64_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_decode_base64_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- URL Encode Section ----
url_encode_section = ctk.CTkFrame(utils_frame)
url_encode_section.pack(pady=10, fill="x")

def run_url_encode():
    text = url_encode_entry.get()
    if text:
        output = url_encode(text)
        terminal_url_encode_output.configure(text=output)
        pyperclip.copy(output) 
    else:
        terminal_url_encode_output.configure(text="Please enter text to URL encode.")
url_encode_button_page_button = ctk.CTkButton(
    url_encode_section,
    text="URL Encode",
    command=lambda: show_frame(url_encode_page),
    fg_color=default_color,
    hover_color=hover_color
)
url_encode_button_page_button.pack(pady=5)

# UI for URL Encode Page
ctk.CTkButton(
    url_encode_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)
ctk.CTkLabel(url_encode_page, text="URL Encode").pack(pady=5)

url_encode_entry = ctk.CTkEntry(url_encode_page, placeholder_text="Enter text to URL encode")

url_encode_entry.pack(pady=5, padx=10, fill="x")
url_encode_button = ctk.CTkButton(
    url_encode_page,
    text="Encode",
    command=run_url_encode,
    fg_color=default_color,
    hover_color=hover_color
)
url_encode_button.pack(pady=5)
terminal_url_encode_output = ctk.CTkLabel(
    url_encode_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_url_encode_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- URL Decode Section ----
url_decode_section = ctk.CTkFrame(utils_frame)
url_decode_section.pack(pady=10, fill="x")

def run_url_decode():
    text = url_decode_entry.get()
    if text:
        output = url_decode(text)
        terminal_url_decode_output.configure(text=output)
        pyperclip.copy(output)
    else:
        terminal_url_decode_output.configure(text="Please enter text to URL decode.")
url_decode_button_page_button = ctk.CTkButton(
    url_decode_section,
    text="URL Decode",
    command=lambda: show_frame(url_decode_page),
    fg_color=default_color,
    hover_color=hover_color
)
url_decode_button_page_button.pack(pady=5)
# UI for URL Decode Page
ctk.CTkButton(
    url_decode_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(url_decode_page, text="URL Decode").pack(pady=5)

url_decode_entry = ctk.CTkEntry(url_decode_page, placeholder_text="Enter URL encoded text to decode")
url_decode_entry.pack(pady=5, padx=10, fill="x")

url_decode_button = ctk.CTkButton(
    url_decode_page,
    text="Decode",
    command=run_url_decode,
    fg_color=default_color,
    hover_color=hover_color
)
url_decode_button.pack(pady=5)

terminal_url_decode_output = ctk.CTkLabel(
    url_decode_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_url_decode_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Random User Agent Section ----
random_user_agent_section = ctk.CTkFrame(utils_frame)
random_user_agent_section.pack(pady=10, fill="x")

def run_random_user_agent():
    output = random_user_agent()
    terminal_random_user_agent_output.configure(text=output)
    pyperclip.copy(output)
random_user_agent_button_page_button = ctk.CTkButton(
    random_user_agent_section,
    text="Random User Agent",
    command=lambda: show_frame(random_user_agent_page),
    fg_color=default_color,
    hover_color=hover_color
)
random_user_agent_button_page_button.pack(pady=5)

# UI for Random User Agent Page
ctk.CTkButton(
    random_user_agent_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(random_user_agent_page, text="Generate Random User Agent").pack(pady=5)

random_user_agent_button = ctk.CTkButton(
    random_user_agent_page,
    text="Generate",
    command=run_random_user_agent,
    fg_color=default_color,
    hover_color=hover_color
)
random_user_agent_button.pack(pady=5)
terminal_random_user_agent_output = ctk.CTkLabel(
    random_user_agent_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_random_user_agent_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Decode JWT Section ----
decode_jwt_section = ctk.CTkFrame(utils_frame)
decode_jwt_section.pack(pady=10, fill="x")
def run_decode_jwt():
    jwt_token = decode_jwt_entry.get()
    if jwt_token:
        output = decode_jwt(jwt_token)
        terminal_decode_jwt_output.configure(text=output)
        pyperclip.copy(output)
    else:
        terminal_decode_jwt_output.configure(text="Please enter a JWT token.")

decode_jwt_button_page_button = ctk.CTkButton(
    decode_jwt_section,
    text="Decode JWT",
    command=lambda: show_frame(decode_jwt_page),
    fg_color=default_color,
    hover_color=hover_color
)
decode_jwt_button_page_button.pack(pady=5)

# UI for Decode JWT Page
ctk.CTkButton(
    decode_jwt_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(decode_jwt_page, text="Decode JWT Token").pack(pady=5)

decode_jwt_entry = ctk.CTkEntry(decode_jwt_page, placeholder_text="Enter JWT token")
decode_jwt_entry.pack(pady=5, padx=10, fill="x")

decode_jwt_button = ctk.CTkButton(
    decode_jwt_page,
    text="Decode",
    command=run_decode_jwt,
    fg_color=default_color,
    hover_color=hover_color
)
decode_jwt_button.pack(pady=5)

terminal_decode_jwt_output = ctk.CTkLabel(
    decode_jwt_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_decode_jwt_output.pack(pady=5, padx=10, fill="both", expand=True)

# ---- Generate UUID Section ----
generate_uuid_section = ctk.CTkFrame(utils_frame)
generate_uuid_section.pack(pady=10, fill="x")

def run_generate_uuid():
    output = generate_uuid()
    terminal_generate_uuid_output.configure(text=output)
    pyperclip.copy(output)
generate_uuid_button_page_button = ctk.CTkButton(
    generate_uuid_section,
    text="Generate UUID",

    command=lambda: show_frame(generate_uuid_page),
    fg_color=default_color,
    hover_color=hover_color
)
generate_uuid_button_page_button.pack(pady=5)

# UI for Generate UUID Page
ctk.CTkButton(
    generate_uuid_page,
    text="Back to Utils",
    command=lambda: show_frame(utils_frame),
    fg_color=default_color,
    hover_color=hover_color
).pack(pady=10)

ctk.CTkLabel(generate_uuid_page, text="Generate UUID").pack(pady=5)

generate_uuid_button = ctk.CTkButton(
    generate_uuid_page,
    text="Generate",
    command=run_generate_uuid,
    fg_color=default_color,
    hover_color=hover_color
)
generate_uuid_button.pack(pady=5)

terminal_generate_uuid_output = ctk.CTkLabel(
    generate_uuid_page,
    text="",
    wraplength=300,
    anchor="nw",
    justify="left",
    fg_color="#1e1e1e",
    text_color="white",
    corner_radius=5
)
terminal_generate_uuid_output.pack(pady=5, padx=10, fill="both", expand=True)

# --------------------------- #
# Start on Home Page
# --------------------------- #
home_frame.pack(fill="both", expand=True)
app.mainloop()
