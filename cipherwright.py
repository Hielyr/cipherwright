import random
from collections import deque

def load_words(file_path):
    # Load words from the specified file and return them as a list
    with open(file_path, 'r') as file:
        return [word.strip() for word in file.readlines()]

def generate_passphrase(words, recent_words, buffer_size):
    # Select words not recently used to avoid repetition
    choice_words = [word for word in words if word not in recent_words]

    # Randomly select two different words
    first_word = random.choice(choice_words).capitalize()
    second_word = random.choice(choice_words).capitalize()

    # Update the list of recent words
    update_recent_words(recent_words, first_word.lower(), buffer_size)
    update_recent_words(recent_words, second_word.lower(), buffer_size)

    # Randomly choose a digit between 2 and 9
    number = random.choice('0123456789')
    # Randomly decide where to place the number (1-4 possible positions)
    position = random.randint(1, 4)

    # Append or prepend the number based on the random position
    if position == 1:
        first_word = number + first_word
    elif position == 2:
        first_word = first_word + number
    elif position == 3:
        second_word = number + second_word
    else:
        second_word = second_word + number

    return f'{first_word}-{second_word}'

def update_recent_words(recent_words, word, buffer_size):
    # Maintain a buffer of recent words to reduce repetition
    if word in recent_words:
        recent_words.remove(word)
    recent_words.append(word)
    # Remove the oldest word if buffer is full
    if len(recent_words) > buffer_size:
        recent_words.popleft()

def main():
    # Load words from the word dictionary file
    words = load_words('CodexVocabulum.txt')
    # Prompt user for the number of passphrases to generate
    num_passphrases = int(input("How many passphrases do you want to generate? "))

    # Size of the buffer to keep track of recently used words
    buffer_size = 32
    recent_words = deque()

    # Generate the specified number of passphrases
    passphrases = [generate_passphrase(words, recent_words, buffer_size) for _ in range(num_passphrases)]

    # Write the generated passphrases to a file
    with open('GrimoireKeys.txt', 'w') as file:
        for passphrase in passphrases:
            file.write(passphrase + '\n')

    print(f"{num_passphrases} passphrases have been generated and saved to GrimoireKeys.txt.")

if __name__ == "__main__":
    main()
