text = "python is good python is easy"

using_words={}

for word in text.split():
    if word not in using_words:
        using_words[word] = 1
    else:
        using_words[word] += 1


print(using_words)