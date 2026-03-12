# personal_text_game
This is for a personal text game i want to try and make

Structure of what needs to be done below:
"""
TEXT-BASED GAME STRUCTURE OVERVIEW
==================================

PROJECT STRUCTURE:

1. PLAYER CLASS
   ├── Attributes:
   │   ├── name (str)
   │   ├── health (int)
   │   ├── max_health (int)
   │   ├── damage (int)
   │   └── is_alive (bool)
   │
   └── Methods:
       ├── __init__() - Initialize player
       ├── take_damage() - Reduce health
       ├── attack() - Deal damage to enemy
       ├── heal() - Restore health
       └── __str__() - Display player status


2. ENEMY CLASS
   ├── Attributes:
   │   ├── name (str)
   │   ├── health (int) - RANDOM VALUE
   │   ├── max_health (int)
   │   ├── damage (int) - RANDOM VALUE
   │   ├── speed (int) - RANDOM VALUE
   │   └── is_alive (bool)
   │
   └── Methods:
       ├── __init__() - Initialize with random stats (using ranges you set)
       ├── take_damage() - Reduce health
       ├── attack() - Deal damage to player
       └── __str__() - Display enemy status


3. GAME CLASS (Main Controller)
   ├── Attributes:
   │   ├── player (Player object)
   │   └── enemies (List of Enemy objects)
   │
   └── Methods:
       ├── __init__() - Set up game
       ├── create_enemies() - Spawn enemies with random stats
       ├── start_game() - Initialize and greet player
       ├── fight_enemy() - Handle turn-based combat loop
       └── run() - Main game loop


4. MAIN LOGIC FLOW
   ├── Welcome player & create Player object
   ├── Create multiple enemies with random stats
   ├── Battle loop:
   │   ├── Display enemy stats (health, damage, speed)
   │   ├── Player chooses action (attack, heal, etc.)
   │   ├── Enemy takes damage or player heals
   │   ├── Enemy attacks back
   │   ├── Check if anyone died
   │   └── Repeat until enemy dies
   ├── Move to next enemy
   └── Game over (win or lose)


KEY FEATURES TO IMPLEMENT:
✓ Random stat generation using random.randint()
✓ Health tracking (current vs max)
✓ Combat system (player vs enemy)
✓ Turn-based gameplay
✓ Status display for all characters
✓ Multiple enemy types with different stat ranges

"""
