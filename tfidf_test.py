import numpy as np

def __get_idf_weights(self, docs: list, vocab: list):
    docs_len = len(docs)
    print(docs_len)
    print("=================")
    weights = {}
    for word in vocab:
        df = 0
        for doc in docs:
            print(doc)
            print("=========doc========")
            df += word in doc
            print(word)
            print("=========df========")
            print(df)
        weights[word] = np.log(docs_len / (df + 1))
        print(weights[word])
        print("=========weights[word]========")
    return [weights[word] for word in vocab]

# 예제 데이터(패킷)
docs = [
    ["utf", "taskmgr", "build","utf"],
    ["masscan", "<script>alert", "kwte"],
    ["gponform", "instance", "totrowcnt", "instance", "instance","utf"],
    ["self", "style", "ghoulsite"],
    # 추가 문서...
    ]

# (tip)
vocab = [
    "utf", "taskmgr", "build", "masscan", "<script>alert", "kwte", "gponform", "instance", "totrowcnt","lil"
]

# 함수 호출
idf_weights = __get_idf_weights(None, docs, vocab)
print(idf_weights)