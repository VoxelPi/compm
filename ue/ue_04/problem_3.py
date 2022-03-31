def sentence_to_list(sentence: str):
    return list(map(lambda word : list(word), sentence.split()))

print(sentence_to_list("i like cake"))

def fibonacci(n):
    result = []
    list(map(lambda x : result.append(x if x <= 1 else result[-1] + result[-2]), range(n)))
    return result

print(fibonacci(10))