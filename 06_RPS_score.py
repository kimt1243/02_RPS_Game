# RPS Component 6 - Scoring System

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item

    if result == "tie":
        result = "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_drawn - rounds_lost

# End of Game statements
print()
print("------ End Game Summary ------")
print(f'Won: {rounds_won} \t/\t Lost: {rounds_lost} \t/\t Drawn: {rounds_drawn}')
print()
print("Thanks for playing")
