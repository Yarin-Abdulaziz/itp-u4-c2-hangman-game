import random

def mask_word(word):
    """Return a masked version of the word."""
    return '*' * len(word)

def uncover_word(answer, masked, guess):
    """Uncover letters in the masked word based on the guessed letter."""
    new_masked = list(masked)
    for index, char in enumerate(answer):
        if char.lower() == guess.lower():
            new_masked[index] = char
    return ''.join(new_masked)

def get_random_word(word_list):
    """Return a random word from the provided list."""
    return random.choice(word_list)

def guess(game, letter):
    """Process a guessed letter and update the game state."""
    if game['game_over']:
        return "Game is already over."
    
    if letter in game['guessed_letters']:
        return "You already guessed that letter."
    
    game['guessed_letters'].add(letter)
    
    if letter in game['answer'].lower():
        game['masked'] = uncover_word(game['answer'], game['masked'], letter)
        if game['masked'] == game['answer']:
            game['game_over'] = True
            return "You've won!"
        return "Good guess!"
    else:
        game['attempts'] -= 1
        if game['attempts'] == 0:
            game['game_over'] = True
            return "You've lost! The word was: " + game['answer']
        return "Wrong guess!"

def start_new_game(word_list):
    """Start a new game of Hangman."""
    answer = get_random_word(word_list)
    game = {
        'answer': answer,
        'masked': mask_word(answer),
        'guessed_letters': set(),
        'attempts': 6,
        'game_over': False
    }
    
    while not game['game_over']:
        print(f"Current word: {game['masked']}")
        guess_letter = input("Guess a letter: ")
        result = guess(game, guess_letter)
        print(result)

# Example word list
if __name__ == "__main__":
    word_list = ["Python", "Java", "C++", "Hangman"]
    start_new_game(word_list)
