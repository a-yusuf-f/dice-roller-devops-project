import random

# Example player stats (replace later with DB)
player_stats = {
    "persuasion": 3,
    "stealth": 5,
    "attack": 4
}

def roll_dice(command):
    command = command.lower()

    for skill in player_stats:
        if skill in command:
            roll = random.randint(1, 20)
            modifier = player_stats[skill]
            total = roll + modifier

            return f"🎲 Rolled {roll} + {modifier} ({skill}) = {total}"

    return "❌ Command not recognised"

# Main loop
while True:
    user_input = input("Say command: ")
    result = roll_dice(user_input)
    print(result)
