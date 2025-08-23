from collections import Counter
from datetime import datetime
import json

print("⏳️ Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def export_to_json(counter, filename=None):
    if not filename:
        filename = f"word_count_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(counter, file, indent=4)
    print(f"📂 Exported to {filename}")

def count_words(text):
    words = text.lower().split()
    count = Counter(words)

    print("\n🔹 Word Frequency:")
    for word, freq in count.most_common():
        print(f"{word}: {freq}")

    print("\nMost common word:", count.most_common(1)[0])

    choice = input("\nDo you want to export this as a .json file? (yes/no): ").strip().lower()
    if choice == "yes":
        export_to_json(count)
    else:
        print("Okay, not exporting...")

def type_and_count():
    text = input("Enter some text (single line): ")
    count_words(text)

def read_and_count():
    file_name = input("Enter the name of the file in the same directory: ")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
            print(f"\nHere comes the content of {file_name}:")
            print("-" * 40)
            print(text)
            print("-" * 40)
            count_words(text)
    except FileNotFoundError:
        print("⁉️ File not found. Make sure it’s in the same directory.")

def file_or_type():
    choice = input("Do you want to `read` from file or `type` your own text? (read/type): ").strip().lower()
    if choice == "read":
        read_and_count()
    elif choice == "type":
        type_and_count()
    else:
        print("Invalid choice. Program exiting...")

file_or_type()
