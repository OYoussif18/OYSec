import subprocess
import platform

def check_sudo_permissions():
    try:
        result = subprocess.check_output("sudo -l", shell=True, text=True)
        return result
    except Exception as e:
        return f"Error checking sudo permissions: {e}"

def find_suid_binaries():
    try:
        result = subprocess.check_output("find / -perm -4000 -type f 2>/dev/null", shell=True, text=True)
        return result
    except Exception as e:
        return f"Error finding SUID binaries: {e}"

def get_kernel_version():
    try:
        return platform.uname().release
    except Exception as e:
        return f"Error getting kernel version: {e}"

def find_writable_files():
    try:
        result = subprocess.check_output("find / -writable -type f 2>/dev/null", shell=True, text=True)
        return result
    except Exception as e:
        return f"Error finding writable files: {e}"

def check_cron_jobs():
    try:
        result = subprocess.check_output("cat /etc/crontab; ls -l /etc/cron*", shell=True, text=True)
        return result
    except Exception as e:
        return f"Error checking cron jobs: {e}"

def search_for_credentials():
    try:
        result = subprocess.check_output("grep -ri 'password\\|passwd\\|secret\\|key' /home 2>/dev/null", shell=True, text=True)
        return result
    except Exception as e:
        return f"Error searching for credentials: {e}"
