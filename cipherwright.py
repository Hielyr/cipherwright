import random
from collections import deque

def load_words(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file.readlines()]

def generate_passphrase(words, recent_words, buffer_size):
    # Select words not in recent words
    choice_words = [word for word in words if word not in recent_words]

    first_word = random.choice(choice_words).capitalize()
    second_word = random.choice(choice_words).capitalize()

    # Update recent words
    update_recent_words(recent_words, first_word.lower(), buffer_size)
    update_recent_words(recent_words, second_word.lower(), buffer_size)

    number = random.choice('23456789')
    if random.choice([True, False]):
        first_word = number + first_word
    else:
        second_word = second_word + number

    return f'{first_word}-{second_word}'

def update_recent_words(recent_words, word, buffer_size):
    if word in recent_words:
        recent_words.remove(word)
    recent_words.append(word)
    if len(recent_words) > buffer_size:
        recent_words.popleft()

def main():
    words = load_words('CodexVocabulum.txt')
    num_passphrases = int(input("How many passphrases do you want to generate? "))
    buffer_size = 10  # Size of the recent words buffer
    recent_words = deque()

    passphrases = [generate_passphrase(words, recent_words, buffer_size) for _ in range(num_passphrases)]

    with open('GrimoireKeys.txt', 'w') as file:
        for passphrase in passphrases:
            file.write(passphrase + '\n')

    print(f"{num_passphrases} passphrases have been generated and saved to GrimoireKeys.txt.")

if __name__ == "__main__":
    main()
