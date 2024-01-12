import random

def load_words(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file.readlines()]

def generate_passphrase(words):
    first_word = random.choice(words).capitalize()
    second_word = random.choice(words).capitalize()
    number = random.choice('23456789')
    # Randomly choose whether to append or prepend the number
    if random.choice([True, False]):
        first_word = number + first_word
    else:
        second_word = second_word + number
    return f'{first_word}-{second_word}'

def main():
    words = load_words('CodexVocabulum.txt')
    num_passphrases = int(input("How many passphrases do you want to generate? "))

    passphrases = [generate_passphrase(words) for _ in range(num_passphrases)]

    with open('GrimoireKeys.txt', 'w') as file:
        for passphrase in passphrases:
            file.write(passphrase + '\n')

    print(f"{num_passphrases} passphrases have been generated and saved to GrimoireKeys.txt.")

if __name__ == "__main__":
    main()
