from collections import Counter
from datetime import datetime

print("⏳️ Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def type_and_count():
    # Ask user for input
    print("Enter some text (single line):")
    text = input("$ ")

    def count_words(text):
        words = text.lower().split()       # lowercase for consistency
        count = Counter(words)

        print("\nMost common word:", count.most_common(1)[0])

    count_words(text)

def read_and_count():
    file_name = input("Enter the name of the file in the same directory: ")
    with open({file_name}, "r") as file:
        print(file.read())

def file_or_type():
    choice = input("Do you want to `read` from file or `type` in the answer?")
    if (choice == "read"):
        read_and_count()
    elif (choice == "type"):
        type_and_count()
    else:
        print("program failed successfully....")

file_or_type()