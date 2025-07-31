import subprocess

def fast_nmap(target):
    result = subprocess.run(["nmap", "-F", "-sV", target, 'T4'], capture_output=True, text=True)
    return result.stdout

def full_nmap(target):
    result = subprocess.run(["nmap", "-sS", "-sV", "-O", target, 'T4'], capture_output=True, text=True)
    return result.stdout

def gobuster_directory(target, wordlist):
    result = subprocess.run(["gobuster", "dir", "-u", target, "-w", wordlist, "-t", "50"], capture_output=True, text=True)
    return result.stdout

def http_headers(target):
    result = subprocess.run(["curl", "-I", target], capture_output=True, text=True)
    return result.stdout

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr