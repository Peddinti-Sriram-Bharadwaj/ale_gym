import sys
from random import randrange
from ale_py import ALEInterface

def main(rom_file):
    ale = ALEInterface()
    ale.setInt("random_seed", 123)
    ale.loadROM(rom_file)

    legal_actions = ale.getLegalActionSet()
    num_actions = len(legal_actions)

    total_reward = 0
    while not ale.game_over():
        a = legal_actions[randrange(num_actions)]
        reward = ale.act(a)
        total_reward += reward
    
    print(f"Episode ended with score: {total_reward}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} rom_file")
        sys.exit(1)
    
    rom_file = sys.argv[1]
    main(rom_file)
