sentence = "i am in awe (fill with happy)"

mood_emojis_dict = {
    "happy": ["🙂", "🤣"]
}

if f"(fill with happy)" in sentence:
    print("found an emoji")
    sentence = sentence.replace(f"(fill with happy)", "")
    words = sentence.split()
else:
    print("not found")

print(words)
print(sentence)

words.append(" ".join(mood_emojis_dict["happy"]))


print(words)

# print
print(" ".join(words))
