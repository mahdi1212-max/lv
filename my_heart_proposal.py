import time
import os
from datetime import datetime
from typing import Optional

CURRENT_TIME = "2025-03-10 14:15:13"
DEVELOPER = "mahdi1212-max"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text: str, delay: float = 0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class HeartToHeart:
    def __init__(self):
        self.first_meeting = "2024-10-15"  # تاریخ اولین آشنایی رو اینجا بذار
        self.coffee_dates = 42  # تعداد قرارهای قهوه خوردن
        self.debug_sessions = 137  # تعداد دفعاتی که همدیگه رو دیباگ کردیم
        self.shared_commits = 1856  # تعداد کامیت‌های مشترک

    async def tell_story(self):
        story = [
            f"\n  Dear fellow developer,",
            f"  It's been {self.debug_sessions} debug sessions together...",
            f"  {self.coffee_dates} coffee breaks sharing our thoughts...",
            f"  {self.shared_commits} commits side by side...",
            "\n  And you know what?",
            "  Every time my code breaks,",
            "  You're the exception I want to catch.",
            "\n  When my system crashes,",
            "  You're my safe recovery mode.",
            "\n  In this infinite loop of life,",
            "  You're the break condition I never want to meet."
        ]
        
        for line in story:
            print_slowly(line)
            time.sleep(0.5)

    def show_commit_log(self):
        commits = [
            ("2024-10-15", "First saw you at the hackathon"),
            ("2024-11-01", "Fixed my broken heart.js"),
            ("2024-12-24", "Merged our holiday plans"),
            ("2025-01-01", "Deployed love to production"),
            ("2025-02-14", "Optimized happiness algorithm"),
            (CURRENT_TIME, "Proposing merge request...")
        ]
        
        print("\n  Git Log: Our Story")
        print("  " + "─" * 50)
        for date, message in commits:
            print(f"  📅 {date}")
            print(f"  └─ 💝 {message}")
            print("  " + "─" * 50)
            time.sleep(0.8)

    def show_metrics(self):
        print("\n  System Health Metrics:")
        metrics = [
            ("Love Level", "█" * 10 + " 100%"),
            ("Trust Rate", "█" * 10 + " 100%"),
            ("Joy Index", "█" * 10 + " 100%"),
            ("Coffee Level", "█" * 3 + "  30%")
        ]
        
        for metric, value in metrics:
            print(f"  {metric:<15} | {value}")
            time.sleep(0.3)

async def main():
    try:
        heart = HeartToHeart()
        
        clear_screen()
        print_slowly("\n  // Initializing heart.js...", 0.1)
        time.sleep(1)
        
        clear_screen()
        await heart.tell_story()
        
        time.sleep(1)
        heart.show_commit_log()
        
        time.sleep(1)
        heart.show_metrics()
        
        print("\n  " + "─" * 50)
        print_slowly('''
  /**
   * Dear You,
   * 
   * They say programming is all about finding solutions
   * to complex problems. But you know what? You're not
   * a problem to solve - you're the solution I never 
   * knew I needed.
   * 
   * Let's pair program for life?
   */
        ''')
        
        print("\n  " + "─" * 50)
        response = input("\n  Execute life.together() (Y/n)? ")
        
        if response.lower() in ['y', 'yes', '']:
            print_slowly("\n  Deploying happiness to production... ✨")
            time.sleep(1)
            print_slowly("  Building our future... 🏠")
            time.sleep(1)
            print_slowly("  Creating infinite joy instances... 💖")
            time.sleep(1)
            print_slowly("\n  Success! Life.together() deployed! 🎉")
        else:
            print_slowly("\n  // Task failed successfully 💔")
            print_slowly("  // But remember: while(alive) { hope(); }")
            
    except KeyboardInterrupt:
        clear_screen()
        print("\n  // Saved in: heart/memories/forever.json")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())