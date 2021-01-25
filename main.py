from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# html5lib
# lxml
# BeautifulSoup4
http = urllib3.PoolManager()

response = http.request('GET',
                        'https://www.lamag.com/article/southern-california-is-having-a-pandemic-real-estate-boom/')
data = response.data
markup = data.decode('utf-8')
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.find_all('p')
wordsArr = []
combinedArr = []
finalArr = []
finalDict = {}
ultimateArr = []
for sentence in tag:
    stringed_sentence = str(sentence)
    # start_of_a_tag = stringed_sentence.find('<a')
    # end_of_a_tag = stringed_sentence.find('</a')
    # if sentence.find('<a') == -1:
    # print(word)
    new_word = stringed_sentence.split(" ")
    wordsArr.append(new_word)

# print(wordsArr)
for arr in wordsArr:
    combinedArr.extend(arr)

for word in combinedArr:
    if word[0:3] == '<p>':
        # print(word)
        # print(word[3:])
        finalArr.append(word[3:])
    elif word[0:4] == '<em>':
        # print(word)
        # print(word[4:])
        finalArr.append(word[4:])
    else:
        finalArr.append(word)

# print(finalArr)

for i, word in enumerate(finalArr):
    count = finalArr.count(word)
    finalDict = {'word': word, 'count': count}

    ultimateArr.append(finalDict)


def sortList(e):
    return e['count']


ultimateArr.sort(reverse=True, key=sortList)
unique_list = pd.DataFrame(ultimateArr).drop_duplicates().to_dict('records')

for item in unique_list:
    print(item)

pd.DataFrame(ultimateArr).drop_duplicates().to_csv('list_of_words.csv',index=False)

# start_location = t.find('the')
# end_location = t.find('</p>')
# print(t)
# print(start_location)
# print(t[start_location:end_location])

# start_location = encoded_data.find('<body')
# end_location = encoded_data.find('</footer>')
# print(encoded_data[start_location:end_location])
