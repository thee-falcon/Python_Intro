def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "🙁",
        ";*": "😘",
        ":3": "🥴",
        ":/": "😕",
        "<3_<3": "😍"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
msg_converter = emoji_converter(message=message)
print(msg_converter)