# ==========================
# Question 1
# ==========================
text = input("Q1 - Enter a word or sentence: ").lower()
vowels = set()

for char in text:
    if char in "aeiou":
        vowels.add(char)

print("Unique vowels found:", vowels)
print("Total unique vowels:", len(vowels))


# ==========================
# Question 2
# ==========================
word_dict = {}
unique_words = set()

num_operations = int(input("\nQ2 - Enter number of operations you want to perform: "))

for _ in range(1, num_operations + 1):
    print("\nMenu inside Dictionary:")
    print("1. Add word")
    print("2. Display all words")
    print("3. Remove word")
    print("4. Exit Dictionary")

    d_choice = input("Enter your choice (1-4): ")

    if d_choice == "1":
        word = input("Enter word: ").strip()
        if word in word_dict:
            print("Word already exists.")
        else:
            meaning = input("Enter meaning: ").strip()
            word_dict[word] = meaning
            unique_words.add(word)
            print("Word added successfully.")

    elif d_choice == "2":
        for w, m in sorted(word_dict.items()):
            print("Word:", w, "Meaning:", m)

    elif d_choice == "3":
        word = input("Enter word to remove: ").strip()
        if word in word_dict:
            word_dict.pop(word)
            unique_words.discard(word)
            print("Word removed successfully.")
        else:
            print("Word not found.")

    elif d_choice == "4":
        break

print("Final set of unique words:", unique_words)


# ==========================
# Question 3
# ==========================
quiz_questions = {
    1: {"question": "What is capital of Nepal?",
        "options": {"A": "Kathmandu", "B": "Pokhara", "C": "Biratnagar", "D": "Lalitpur"},
        "answer": "A"},
    2: {"question": "What is 2 + 2?",
        "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
        "answer": "B"},
    3: {"question": "Which planet is called Red Planet?",
        "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
        "answer": "B"}
}

score = 0

for k in quiz_questions:
    print("\nQuestion:", quiz_questions[k]["question"])
    for option in quiz_questions[k]["options"]:
        print(option, ":", quiz_questions[k]["options"][option])

    user_ans = input("Enter your choice (A/B/C/D): ").upper()

    if user_ans == quiz_questions[k]["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is", quiz_questions[k]["answer"])

print("Your final score:", score, "out of", len(quiz_questions))


# ==========================
# Question 4
# ==========================
num_items = int(input("\nQ4 - Enter total number of items purchased: "))
prices = []

for i in range(1, num_items + 1):
    price = float(input("Enter price of item " + str(i) + ": "))
    prices.append(price)

total = sum(prices)
print("Total cost of items:", total)


# ==========================
# Question 5
# ==========================
sentence = input("\nQ5 - Enter a full sentence: ")
words = sentence.split()
total_words = len(words)

unique_words_set = set()
for word in words:
    unique_words_set.add(word.lower())

print("Total words:", total_words)
print("Unique words:", len(unique_words_set))


# ==========================
# Question 6
# ==========================
sentence = input("\nQ6 - Enter a sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    w = word.lower()
    word_count[w] = word_count.get(w, 0) + 1

for w in sorted(word_count):
    print(w + ":", word_count[w])# ==========================
# Question 1
# ==========================
text = input("Q1 - Enter a word or sentence: ").lower()
vowels = set()

for char in text:
    if char in "aeiou":
        vowels.add(char)

print("Unique vowels found:", vowels)
print("Total unique vowels:", len(vowels))


# ==========================
# Question 2
# ==========================
word_dict = {}
unique_words = set()

num_operations = int(input("\nQ2 - Enter number of operations you want to perform: "))

for _ in range(1, num_operations + 1):
    print("\nMenu inside Dictionary:")
    print("1. Add word")
    print("2. Display all words")
    print("3. Remove word")
    print("4. Exit Dictionary")

    d_choice = input("Enter your choice (1-4): ")

    if d_choice == "1":
        word = input("Enter word: ").strip()
        if word in word_dict:
            print("Word already exists.")
        else:
            meaning = input("Enter meaning: ").strip()
            word_dict[word] = meaning
            unique_words.add(word)
            print("Word added successfully.")

    elif d_choice == "2":
        for w, m in sorted(word_dict.items()):
            print("Word:", w, "Meaning:", m)

    elif d_choice == "3":
        word = input("Enter word to remove: ").strip()
        if word in word_dict:
            word_dict.pop(word)
            unique_words.discard(word)
            print("Word removed successfully.")
        else:
            print("Word not found.")

    elif d_choice == "4":
        break

print("Final set of unique words:", unique_words)


# ==========================
# Question 3
# ==========================
quiz_questions = {
    1: {"question": "What is capital of Nepal?",
        "options": {"A": "Kathmandu", "B": "Pokhara", "C": "Biratnagar", "D": "Lalitpur"},
        "answer": "A"},
    2: {"question": "What is 2 + 2?",
        "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
        "answer": "B"},
    3: {"question": "Which planet is called Red Planet?",
        "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
        "answer": "B"}
}

score = 0

for k in quiz_questions:
    print("\nQuestion:", quiz_questions[k]["question"])
    for option in quiz_questions[k]["options"]:
        print(option, ":", quiz_questions[k]["options"][option])

    user_ans = input("Enter your choice (A/B/C/D): ").upper()

    if user_ans == quiz_questions[k]["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is", quiz_questions[k]["answer"])

print("Your final score:", score, "out of", len(quiz_questions))


# ==========================
# Question 4
# ==========================
num_items = int(input("\nQ4 - Enter total number of items purchased: "))
prices = []

for i in range(1, num_items + 1):
    price = float(input("Enter price of item " + str(i) + ": "))
    prices.append(price)

total = sum(prices)
print("Total cost of items:", total)


# ==========================
# Question 5
# ==========================
sentence = input("\nQ5 - Enter a full sentence: ")
words = sentence.split()
total_words = len(words)

unique_words_set = set()
for word in words:
    unique_words_set.add(word.lower())

print("Total words:", total_words)
print("Unique words:", len(unique_words_set))


# ==========================
# Question 6
# ==========================
sentence = input("\nQ6 - Enter a sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    w = word.lower()
    word_count[w] = word_count.get(w, 0) + 1

for w in sorted(word_count):
    print(w + ":", word_count[w])
