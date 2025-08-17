import time
import os
from datetime import datetime, timedelta
from typing import List, Dict

# اینا رو می‌تونی تغییر بدی
FIRST_DEBUG = "2024-09-15"  # تاریخ اولین دیباگ
PULL_REQUESTS = 23  # تعداد PR هایی که روش کار کردین
REPOSITORY = "awesome-project"  # اسم پروژه‌ای که توش همکاری داشتین

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_typing(text: str, delay: float = 0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class DebugStory:
    def __init__(self):
        self.debug_sessions = {
            "fixed": 47,
            "pending": 3,
            "special": 1  # این خواستگاری :)
        }
        self.lines_reviewed = 14328
        self.late_night_commits = 56

    def show_first_encounter(self):
        story = [
            "\n  // First encounter in the codebase",
            f"  git blame {REPOSITORY}/core/system.js",
            "  ...",
            f"  // Author: her-username",
            "  // Date: {FIRST_DEBUG}",
            "  // Message: Fixed critical bug in main logic",
            "",
            "  // My thoughts that day:",
            "  /** ",
            "   * I noticed how elegantly you solved that bug",
            "   * Your code was poetry in motion",
            "   * Never seen someone debug with such grace",
            "   * That's when I knew you were different",
            "   */"
        ]
        for line in story:
            print_typing(line)
            time.sleep(0.2)

    def show_collaboration_stats(self):
        print("\n  === Our Code Journey ===")
        stats = [
            (f"Pull Requests Reviewed Together: {PULL_REQUESTS}", "🔍"),
            (f"Lines of Code We've Shared: {self.lines_reviewed}", "📝"),
            (f"Late Night Debug Sessions: {self.late_night_commits}", "🌙"),
            (f"Days Since First Code Review: {(datetime.now() - datetime.strptime(FIRST_DEBUG, '%Y-%m-%d')).days}", "📅")
        ]
        
        for stat, emoji in stats:
            print(f"  {emoji} {stat}")
            time.sleep(0.5)

    def show_debug_logs(self):
        debug_moments = [
            ("TypeError", "Realized I couldn't stop thinking about your code"),
            ("Uncaught Exception", "Your comments made me smile"),
            ("Memory Leak", "Lost sleep thinking about our next code review"),
            ("Infinite Loop", "Found myself checking your PRs again and again"),
            ("Syntax Error", "Tried to explain how I feel in code"),
            ("Runtime Error", "My heart skips a beat when you approve my PR")
        ]
        
        print("\n  🔍 Debug Log Analysis:")
        print("  " + "─" * 50)
        for error, moment in debug_moments:
            print(f"  Exception: {error}")
            print(f"  Message: {moment}")
            print("  " + "─" * 50)
            time.sleep(0.7)

async def main():
    try:
        story = DebugStory()
        
        clear_terminal()
        print_typing("\n  Initializing debug session...", 0.1)
        time.sleep(1)
        
        clear_terminal()
        print_typing('''
  /**
   * Dear Code Reviewer,
   * 
   * They say the best code is self-documenting
   * But my feelings for you need comments
   * Because every bug you find in my code
   * Makes my heart compile faster
   */
        ''')
        
        time.sleep(2)
        story.show_first_encounter()
        
        time.sleep(1)
        story.show_collaboration_stats()
        
        time.sleep(1)
        story.show_debug_logs()
        
        print("\n  " + "─" * 50)
        print_typing('''
  /**
   * I know we've never met in person
   * But through your code, I see your soul
   * Each PR shows me your brilliance
   * Every comment reveals your kindness
   * 
   * Would you like to debug life together?
   * Promise I'm better at relationships than at coding
   * 
   * @param {You} partner
   * @returns {Future} ourLife
   */
   ''')
        
        print("\n  " + "─" * 50)
        response = input("\n  accept merge request (Y/n)? ")
        
        if response.lower() in ['y', 'yes', '']:
            print_typing("\n  Merging hearts...")
            time.sleep(1)
            print_typing("  Creating shared repository...")
            time.sleep(1)
            print_typing("  Deploying happiness.js...")
            time.sleep(1)
            print_typing("\n  Merge successful! ✨")
        else:
            print_typing("\n  // No worries, keeping main branch stable")
            print_typing("  // Maybe I need more unit tests for my heart")
            
    except KeyboardInterrupt:
        clear_terminal()
        print("\n  // Debug session saved in: heart/memories/first_attempt.log")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())