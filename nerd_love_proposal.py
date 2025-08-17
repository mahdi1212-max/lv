import os
import time
import random
from typing import List, Dict, Optional
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_walking_scene():
    scenes = [
        # Scene 1: Initial approach with laptop
        [
            "     O       O    ",
            "    /|\\     /|\\   ",
            "    / \\     / \\   ",
            "   [|_|]          ",
            "   -->            ",
            "Debugging life..."
        ],
        # Scene 2: Getting closer
        [
            "       O     O    ",
            "      /|\\   /|\\   ",
            "      / \\   / \\   ",
            "     [|_|]        ",
            "     -->          ",
            "Compiling love..."
        ],
        # Scene 3: Almost there
        [
            "         O   O    ",
            "        /|\\ /|\\   ",
            "        / \\ / \\   ",
            "       [|_|]      ",
            "       -->        ",
            "git push heart..."
        ],
        # Scene 4: Together
        [
            "          O O     ",
            "         /|\\/|\\   ",
            "         / \\/ \\   ",
            "        [|_|]     ",
            "     Loading...   ",
            "async love(you)..."
        ],
        # Scene 5: The proposal
        [
            "         \\O O/    ",
            "          |\\|     ",
            "         / | \\    ",
            "        [|_|]     ",
            "    while True:   ",
            "      love(you)   "
        ]
    ]
    
    for scene in scenes:
        clear_screen()
        print("\n" * 2)
        print('\n'.join(scene))
        time.sleep(1)

def show_code_rain():
    love_tokens = [
        'heart += 1', 'love.append(you)', 'us.together()', 
        'await love', 'yield happiness', 'return hearts',
        'if love: kiss()', 'def love():', 'class Together:',
        'import happiness', 'love is True', 'while love:'
    ]
    
    width = 60
    height = 15
    
    for _ in range(15):  # کمتر کردم که خسته کننده نباشه
        clear_screen()
        for _ in range(height):
            line = ''
            for _ in range(width // 10):
                if random.random() < 0.3:
                    line += random.choice(love_tokens).ljust(10)
                else:
                    line += ' ' * 10
            print(line)
        time.sleep(0.1)

def show_happy_ending():
    endings = [
        # Frame 1: Success!
        [
            "",
            "    *~*~*~*~*~*~*~*~*~*~*~*",
            "    *                      *",
            "    *  Compilation Success! *",
            "    *                      *",
            "    *~*~*~*~*~*~*~*~*~*~*~*",
            "",
            "          O-O",
            "         /|~|\\",
            "        [|_|] \\",
            "         / | \\",
            "",
            "    Build: SUCCESS ✓",
            "    Tests: PASSED ✓",
            "    Love: INFINITE ∞",
            ""
        ],
        # Frame 2: Together
        [
            "",
            "    *~*~*~*~*~*~*~*~*~*~*~*",
            "    *                      *",
            "    *    git merge heart   *",
            "    *                      *",
            "    *~*~*~*~*~*~*~*~*~*~*~*",
            "",
            "          O-O",
            "         /|~|\\",
            "         |_| \\",
            "         / | \\",
            "",
            "    Status: 200 OK",
            "    Cache: Forever",
            "    Type: True Love",
            ""
        ]
    ]
    
    for _ in range(3):  # تکرار انیمیشن
        for frame in endings:
            clear_screen()
            print('\n'.join(frame))
            time.sleep(0.8)

class CodeProposal:
    def __init__(self):
        self.status: Dict[str, bool] = {
            "compilation": True,
            "testing": True,
            "deployment": True
        }

    def show_proposal(self):
        proposal_code = [
            "class LoveProposal(LifeEvent):",
            "    def __init__(self, you, me):",
            "        self.date = '2025-03-10'",
            f"        self.author = '{os.getenv('USER', 'mahdi1212-max')}'",
            "        self.love = float('inf')",
            "",
            "    @forever_together",
            "    async def propose(self) -> bool:",
            "        try:",
            "            while self.love == float('inf'):",
            "                await self.share_life_with(you)",
            "                self.happiness += 1",
            "            return True",
            "        except LonelinessError:",
            "            return self.try_again()",
            "",
            "    def compile_future(self):",
            "        return {",
            "            'love': 'growing',",
            "            'bugs': 0,",
            "            'features': ['trust', 'care', 'joy'],",
            "            'deployment': 'lifetime'",
            "        }",
            "",
            "# Will you git commit to our love? ❤️"
        ]
        
        for line in proposal_code:
            print(f"  {line}")
            time.sleep(0.15)

def main():
    try:
        print("\n  Loading love module...")
        time.sleep(1)
        
        # نمایش بارش کد
        show_code_rain()
        
        # نمایش انیمیشن راه رفتن
        show_walking_scene()
        
        # نمایش کد خواستگاری
        clear_screen()
        print("\n" * 2)
        proposal = CodeProposal()
        proposal.show_proposal()
        
        # دریافت پاسخ
        print("\n" * 2)
        while True:
            answer = input("  $ git commit -m 'respond' (Y/n): ").strip().lower()
            if answer in ['y', 'yes', '']:
                clear_screen()
                print("\n" * 2)
                show_happy_ending()
                break
            elif answer in ['n', 'no']:
                print("\n  // Fatal Error: HeartBreakException")
                print("  // Stack trace: love.py, line 143, in propose()")
                print("  // Debug required... 💔")
                break
            else:
                print("  // SyntaxError: Invalid response format")

    except KeyboardInterrupt:
        clear_screen()
        print("\n  // Process terminated: SIGINT")
        print("  // Saving progress... love.tmp")

if __name__ == "__main__":
    main()