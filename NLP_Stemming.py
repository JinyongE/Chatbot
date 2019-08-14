# -*- coding:utf-8 -*-
import urllib3
import json
import numpy as np
from ast import literal_eval

# 형태소 분석을 위한 문장 입력
print('형태소 분석을 위한 문장을 입력하세요 : ')
input_text = input()

#형태소 분석 API
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
accessKey = "6b733776-eb43-4a97-aaef-78fb70b5cc0d"
analysisCode = "morp"
text = str(input_text)

requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)

# print("[responseCode] " + str(response.status))
# print("[responBody]")
# print(str(response.data, "utf-8"))
# 추가된 코드(토큰화된 형태소들의 리스트를 변수)
# print(str(response.data["morp"], "utf-8"))
# str(response.data, "utf-8"
# print(type(response.data))

X = str(response.data, "utf-8")
dict_X = literal_eval(X)
# print(type(dict_X))
# print(dict_X)

dict_X2 = dict_X['return_object']['sentence'][0]
# print(type(dict_X2))
# print(dict_X2)

tokenslist = dict_X2['morp']

# 최종적으로 토큰화, 형태소 정보 딕셔너리 형태들의 리스트로 반환
# tokenslist[i]
# {'id': 0.0, 'lemma': '안녕', 'type': 'NNG', 'position': 0.0, 'weight': 0.187449}
# {'id': 1.0, 'lemma': '하', 'type': 'XSA', 'position': 6.0, 'weight': 0.0001}
# {'id': 2.0, 'lemma': '시', 'type': 'EP', 'position': 9.0, 'weight': 0.0173731}
# {'id': 3.0, 'lemma': 'ㅂ니까', 'type': 'EF', 'position': 9.0, 'weight': 0.637434}
# {'id': 4.0, 'lemma': '!', 'type': 'SF', 'position': 18.0, 'weight': 1.0}


# 변수 선언
tokenslist_id = list()

for i in range(len(tokenslist)):
    tokenslist_id.append(tokenslist[i]['id'])

tokenslist_lemma = list()

for i in range(len(tokenslist)):
    tokenslist_lemma.append(tokenslist[i]['lemma'])

tokenslist_type = list()

for i in range(len(tokenslist)):
    tokenslist_type.append(tokenslist[i]['type'])

tokenslist_position = list()

for i in range(len(tokenslist)):
    tokenslist_position.append(tokenslist[i]['position'])

tokenslist_weight = list()

for i in range(len(tokenslist)):
    tokenslist_weight.append(tokenslist[i]['weight'])

'''
# 선언된 변수들
print(tokenslist)
print(tokenslist_id)
print(tokenslist_lemma)
print(tokenslist_type)
print(tokenslist_position)
print(tokenslist_weight)
'''

# word2vec 위한 딕셔너리 생성
word_to_id = {}
for i in range(len(tokenslist)):
    word_to_id.update({tokenslist[i]['lemma']:tokenslist[i]['id']})

id_to_word = {}
for i in range(len(tokenslist)):
    id_to_word.update({tokenslist[i]['id']:tokenslist[i]['lemma']})

print("word_to_id : ", word_to_id)
print("id_to_word : ", id_to_word)





####### 말뭉치(corpus) 생성  #######

corpus_text = open('training_corpus_exbrain.txt', 'r', encoding='utf-8')
corpus_text = corpus_text.read()
print(corpus_text)



#형태소 분석 API
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
accessKey = "6b733776-eb43-4a97-aaef-78fb70b5cc0d"
analysisCode = "morp"
text1 = str(corpus_text)

requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text1,
        "analysis_code": analysisCode
    }
}

http = urllib3.PoolManager()
corpus_response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)


# print(corpus_response.data)
# 추가된 코드(토큰화된 형태소들의 리스트를 변수)
# print(str(response.data["morp"], encoding= "utf-8"))
# str(response.data, "utf-8"
# print(type(response.data))

original_corpus = str(corpus_response.data, "utf-8")
# print(original_corpus)

dict_original_corpus = literal_eval(original_corpus)
dict2_original_corpus = dict_original_corpus['return_object']['sentence'][0]
corpus_tokenslist = dict2_original_corpus['morp']

# 최종적으로 토큰화, 형태소 정보 딕셔너리 형태들의 리스트로 반환
# corpus_tokenslist[i]
# {'id': 0.0, 'lemma': '안녕', 'type': 'NNG', 'position': 0.0, 'weight': 0.187449}
# {'id': 1.0, 'lemma': '하', 'type': 'XSA', 'position': 6.0, 'weight': 0.0001}
# {'id': 2.0, 'lemma': '시', 'type': 'EP', 'position': 9.0, 'weight': 0.0173731}
# {'id': 3.0, 'lemma': 'ㅂ니까', 'type': 'EF', 'position': 9.0, 'weight': 0.637434}
# {'id': 4.0, 'lemma': '!', 'type': 'SF', 'position': 18.0, 'weight': 1.0}


# 변수 선언
corpus_tokenslist_id = list()

for i in range(len(corpus_tokenslist)):
    corpus_tokenslist_id.append(corpus_tokenslist[i]['id'])

corpus_tokenslist_lemma = list()

for i in range(len(corpus_tokenslist)):
    corpus_tokenslist_lemma.append(corpus_tokenslist[i]['lemma'])

corpus_tokenslist_type = list()

for i in range(len(corpus_tokenslist)):
    corpus_tokenslist_type.append(corpus_tokenslist[i]['type'])

corpus_tokenslist_position = list()

for i in range(len(corpus_tokenslist)):
    corpus_tokenslist_position.append(corpus_tokenslist[i]['position'])

corpus_tokenslist_weight = list()

for i in range(len(corpus_tokenslist)):
    corpus_tokenslist_weight.append(corpus_tokenslist[i]['weight'])

# word2vec 위한 딕셔너리 생성
# corpus_word_to_id = {}
# for i in range(len(corpus_tokenslist)):
#     corpus_word_to_id.update({corpus_tokenslist[i]['lemma']:corpus_tokenslist[i]['id']})
#
# corpus_id_to_word = {}
# for i in range(len(corpus_tokenslist)):
#     corpus_id_to_word.update({corpus_tokenslist[i]['id']:corpus_tokenslist[i]['lemma']})
#
# corpus = np.array([corpus_word_to_id[w] for w in corpus_word_to_id.keys()])


words = corpus_tokenslist_lemma
# print(words)
corpus_word_to_id = {}
corpus_id_to_word = {}

for word in words:
    if word not in corpus_word_to_id:
        new_id = len(corpus_word_to_id)
        corpus_word_to_id[word] = new_id
        corpus_id_to_word[new_id] = word

corpus = [corpus_word_to_id[w] for w in words]
corpus = np.array(corpus)

print("\n")
print("<<corpus information>>\n")
print("corpus : ", corpus)
print("corpus_word_to_id : ", corpus_word_to_id)
print("corpus_id_to_word : ", corpus_id_to_word)
#

