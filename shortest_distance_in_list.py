def word_index(word, l):
    if not find_duplicates(word, l):
        ind = l.index(word)
        return ind
    else:
        index_list = []
        count = -1
        for wrd in l:
            count += 1
            if wrd == word:
                index_list.append(count)
        return index_list

def find_duplicates(word, l):
    counts = l.count(word)
    if counts > 1:
        return True

l = ["practice", "makes", "perfect", "coding", "makes", "coding"]

word1 = "practice"
word2 = "coding"

index_word1 = word_index(word1, l)
index_word2 = word_index(word2, l)

if type(index_word1) is list and type(index_word2) is list:
    index_diff = []
    for i in index_word1:
        for j in index_word2:
            index_diff.append(abs(j - i))
    diff = min(index_diff)
    print(f"The closest distance between {word1} and {word2} is {diff}")

elif type(index_word1) is not list and type(index_word2) is not list:
    diff = abs(index_word2 - index_word1)
    print(f"The closest distance between {word1} and {word2} is {diff} away")

elif type(index_word1) is not list and type(index_word2) is list:
    index_diff = []
    for i in index_word2:
        index_diff.append(abs(i - index_word1))
    diff = min(index_diff)
    print(f"The closest distance between {word1} and {word2} is {diff} away")

elif type(index_word1) is list and type(index_word2) is not list:
    index_diff = []
    for i in index_word1:
        index_diff.append(abs(i - index_word2))
    diff = min(index_diff)
    print(f"The closest distance between {word1} and {word2} is {diff} away")
