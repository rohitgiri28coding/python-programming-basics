def mergeAlternately(word1: str, word2: str) -> str:
    res = ''.join([word1[i] + word2[i] for i in range(min(len(word1), len(word2)))])
    res = res + word1[len(word2):len(word1)] if len(word1) > len(word2) else res + word2[len(word1):len(word2)] if len(
        word1) < len(word2) else res
    return res


print(mergeAlternately('abc', 'pqrs'))
