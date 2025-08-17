import os
import time
import random
import sys
from datetime import datetime

CURRENT_TIME = "2025-03-10 14:33:22"
HACKER = "mahdi1212-max"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_bar(text, duration=20):
    for i in range(duration):
        clear_screen()
        percent = (i + 1) * 100 // duration
        bar = '=' * (i + 1) + ' ' * (duration - i - 1)
        print(f"{text}: [{bar}] {percent}%")
        time.sleep(0.1)

def fake_hack_screen():
    ip_addresses = [
        "192.168.1.1", "10.0.0.1", "172.16.0.1",
        "127.0.0.1", "169.254.0.1", "192.0.2.1"
    ]
    
    ports = [21, 22, 80, 443, 3306, 5432, 27017]
    
    services = [
        "SSH", "HTTP", "FTP", "SMTP", 
        "MySQL", "PostgreSQL", "MongoDB"
    ]
    
    for _ in range(15):
        ip = random.choice(ip_addresses)
        port = random.choice(ports)
        service = random.choice(services)
        status = random.choice(["SCANNING", "CONNECTING", "PROBING"])
        
        print(f"[*] {status} {ip}:{port} ({service})")
        time.sleep(0.2)

def show_binary_heart():
    heart = [
        "    0101010    0101010    ",
        "   01  1  10  01  1  10   ",
        "  011    110011    110  ",
        "  010     11111     010  ",
        "   010     111     010   ",
        "    010    111    010    ",
        "     010   111   010     ",
        "      010  111  010      ",
        "       010 111 010       ",
        "        010101010        ",
        "         101110         ",
        "          0110          ",
        "           11           "
    ]
    
    colors = ['\033[91m', '\033[92m', '\033[94m', '\033[96m']
    reset = '\033[0m'
    
    for line in heart:
        color = random.choice(colors)
        print(f"{color}{line}{reset}")
        time.sleep(0.1)

def main():
    try:
        clear_screen()
        type_effect("\n[*] Initiating system breach...", 0.03)
        time.sleep(1)
        
        loading_bar("Bypassing security")
        
        clear_screen()
        print("[*] Accessing mainframe...\n")
        fake_hack_screen()
        
        clear_screen()
        type_effect("\n[!] WARNING: Unexpected emotional protocol detected!", 0.03)
        time.sleep(1)
        
        print("\n[*] Analyzing core system files...")
        time.sleep(1)
        
        loading_bar("Decrypting heart.dat")
        
        clear_screen()
        type_effect("\n[*] CRITICAL: System compromised by feelings.exe!", 0.03)
        time.sleep(1)
        
        print("\n[*] Encrypted message found...")
        time.sleep(1)
        
        type_effect("\n[*] Decoding message...", 0.03)
        time.sleep(1)
        
        clear_screen()
        show_binary_heart()
        
        message = f"""
[DECODED MESSAGE START]
╔══════════════════════════════════════╗
║  Target: Your Heart                  ║
║  Status: Under Attack               ║
║  Method: Love Overflow              ║
║  Source: {HACKER}                    ║
╚══════════════════════════════════════╝

[SYSTEM ANALYSIS]
• First contact: Code review #1337
• Vulnerability found: Your brilliant mind
• Attack vector: Your amazing skills
• System weakness: Your beautiful soul

[EXPLOIT DETAILS]
I've been tracking your code
Every line you write makes my heart race
Your algorithms are pure poetry
Your bugs are cuter than features

[PROPOSED SOLUTION]
Let's merge our repositories
Format our future together
Debug life as one unit
No need for exception handling

[!] Critical decision required...
        """
        
        type_effect(message, 0.02)
        
        choice = input("\n[?] Accept connection request? (Y/n): ")
        
        if choice.lower() in ['y', 'yes', '']:
            clear_screen()
            type_effect("\n[✓] Connection established!", 0.03)
            time.sleep(1)
            type_effect("[✓] Hearts synchronized!", 0.03)
            time.sleep(1)
            type_effect("[✓] Future.exe launched successfully!", 0.03)
            time.sleep(1)
            show_binary_heart()
        else:
            clear_screen()
            type_effect("\n[!] Connection attempt failed", 0.03)
            time.sleep(1)
            type_effect("[*] Implementing retry algorithm...", 0.03)
            time.sleep(1)
            type_effect("[*] Hope.exe still running...", 0.03)
    
    except KeyboardInterrupt:
        clear_screen()
        print("\n[!] Emergency system shutdown initiated")
        print("[*] Feelings safely stored in backup.love")

if __name__ == "__main__":
    main()