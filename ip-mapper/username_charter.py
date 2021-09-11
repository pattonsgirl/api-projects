import csv
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# putting the usernames and ips into a list so I can use them later
with open("data/auth.logs.csv", 'r') as f:
    reader = csv.reader(f)
    usernames, ips = [], []

    for row in reader:
        usernames.append(row[0].strip())
        ips.append(row[1].strip())

# print first 10 as proof
print(ips[:10])
print(len(ips))

print(len(usernames))

nd_usernames = []
for  username in usernames:
    if username not in nd_usernames:
        nd_usernames.append(username)

print(len(nd_usernames))

print(usernames[:10])
print(nd_usernames[:10])

# the wordcloud library only accepts a string, so made a giant string of username values
# tutorial: https://www.python-graph-gallery.com/wordcloud/
string_unames = (" ".join(usernames))
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(string_unames)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

# https://programminghistorian.org/en/lessons/counting-frequencies

# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


dictionary = wordListToFreqDict(usernames)
sorteddict = sortFreqDict(dictionary)

top_ten_names, top_ten_occurences = [], []
for s in sorteddict[:10]: 
    # output in markdown for easier use in documentation
    print(f"- Username **{s[1]}** is used {s[0]} times")
    top_ten_names.append(s[1])
    top_ten_occurences.append(s[0])

# https://pythonbasics.org/matplotlib-bar-chart/
plt.figure()
# unsorted chart
#ax.bar(dictionary.keys(), dictionary.values())
plt.bar(top_ten_names, top_ten_occurences, color = 'orange', width = 0.5)
plt.grid(color='royalblue', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

plt.title('Top Ten Usernames Attempted')
plt.xlabel('Username')
plt.ylabel('Occurences in Log');

plt.show()