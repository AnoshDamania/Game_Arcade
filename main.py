import Snake_like_game
import Tic_Tac_toe
import Def_Not_Dino
import Stiff_bird

print("Hello There.... Welcome to the game Arcade")
print("Choose what you want to play:")
print("Enter 1 to play SNAKE LIKE GAME,")
print("Enter 2 to play TIC_TAC_TOE,")
print("Enter 3 to play DEF Not DINO,")
print("Enter anything else to play STIFF BIRD")

x = input()

if input == '1':
    Snake_like_game.run_all()
elif input == '2':
    Tic_Tac_toe.run_all()
elif input == '3':
    Def_Not_Dino.run_all()
else:
    Stiff_bird.run_all()
