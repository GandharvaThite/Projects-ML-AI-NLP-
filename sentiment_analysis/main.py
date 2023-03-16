import string
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words = cleaned_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "but"]
final_words = []

for i in range(len(tokenized_words)):
    if(tokenized_words[i] not in stop_words):
        final_words.append(tokenized_words[i])

emotion_list = []
with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

plain_emo = []
for i in emotion_list:
    if(i not in plain_emo):
        plain_emo.append(i)
count_emo = []
for i in range(len(plain_emo)):
    count_emo.append(0)
for i in range(len(plain_emo)):
    for j in range(len(emotion_list)):
        if(plain_emo[i]==emotion_list[j]):
            count_emo[i]+=1
dominant_emotions = max(count_emo)

ans = []
for i in range(len(count_emo)):
    if(count_emo[i] == dominant_emotions):
        ans.append(plain_emo[i])
if(len(ans)>1):
    print("The following text depicts multiple emotions:-",ans)
if(len(ans)==1):
    print("The following text depicts single emotion:-",ans[0])


