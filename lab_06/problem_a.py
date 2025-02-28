# CLI tool to translate words into emojis and fill with entered mood

# emoji dictionary
emoji_dict = {
    "love": "❤️",
    "happy": "😀",
    "birthday": "🎂",
    "namaste": "🙏🏻",
    "girl": "🙅‍♀️💁‍♀️",
    "nature": "🍀"
}

mood_emojis_dict = {
    "happy": ["🙂", "🤣"],
    "sad": ["😭", "😢"]
}


def emoji_translator(sentence):
    words = sentence.split()
    translated_emojis = [word if emoji_dict.get(
        word.lower()) == None else emoji_dict.get(word.lower()) for word in words]
    return " ".join(translated_emojis)


def mood_fill_emojis(sentence):

    mood = ""
    for key in mood_emojis_dict:
        target_mood = f"(fill with {key})"
        if target_mood in sentence:
            # replace with emojis
            mood = key
            sentence = sentence.replace(target_mood, "")
            break

    if mood:
        words = sentence.split()
        words.append(" ".join(mood_emojis_dict[mood]))
        return " ".join(words)

    else:
        return sentence


if __name__ == "__main__":
    print("🎉 Welcome to Emoji Translator CLI Tool 🎉")
    print("Select an option (1-3) to proceed")
    print("1. Emoji Translator")
    print("2. Mood autofill")
    print("3. Exit")

    user_choice = int(input("Enter your option: "))

    match(user_choice):
        case 1:
            print("Lets transalte your words into emojis...")
            sentence = input("Enter the words you want to translate: ")
            print(emoji_translator(sentence))
        case 2:
            print("Lets fill your mood with emojis...")
            sentence = input(
                "Enter the mood you want to fill with emojis. e.g. I am feeling good (fill with love): ")
            print(mood_fill_emojis(sentence))
        case 3:
            print("Exiting the tool...")
