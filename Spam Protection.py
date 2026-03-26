spam_words = ["winner", "money", "offer","lottery", "prize", "cash","click","buy", "limited","congratulations", "claim" ]
def spam_score(email):
    email = email.lower()
    score = 0
    for word in spam_words:
        if word in email:
            score += 1
    return score
def classify_email(email):
    score = spam_score(email)
    if score >= 3:
        return "SPAM"
    elif score == 2:
        return "SUSPICIOUS"
    else:
        return "NOT SPAM"
def single_email():
    email = input("Enter Email Message:")
    result = classify_email(email)
    score = spam_score(email)
    print("Spam Score:", score)
    print("Result:", result)
def check_file():
    try:
        file = open("emails.txt", "r")
        print("Checking Emails from File")
        for line in file:
            email = line.strip()
            score = spam_score(email)
            result = classify_email(email)
            print("Email:", email)
            print("Score:", score)
            print("Result:", result)
        file.close()
    except:
        print("emails.txt file not found")
def spam_word():
    word = input("Enter new spam word: ")
    spam_words.append(word.lower())
    print("Spam word added successfully!")
def save_result():
    email = input("Enter Email Message:")
    score = calculate_spam_score(email)
    result = classify_email(email)
    file = open("results.txt", "a")
    file.write(email + " --> " + result + "\n")
    file.close()
    print("Result saved to results.txt")
def menu():
    while True:
        print(" Spam Mail Protection System")
        print("1. Check Single Email")
        print("2. Check Emails from File")
        print("3. Add Spam Word")
        print("4. Save Email Result")
        print("5. Show Spam Words")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_single_email()
        elif choice == "2":
            check_file()
        elif choice == "3":
            add_spam_word()
        elif choice == "4":
            save_result()
        elif choice == "5":
            print("\nSpam Words List:")
            for word in spam_words:
                print("-", word)
        elif choice == "6":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice")
menu()
