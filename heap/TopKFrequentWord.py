from typing import List
import heapq

def topKFrequent(words: List[str], k: int) -> List[str]:

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    heap = []

    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))

    return [heapq.heappop(heap)[1] for _ in range(k)]



if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 2

    print(topKFrequent(words, k))
