#encoding: utf-8

class Dict:
    def __init__(self):
        self._words = {}

    def addWords(self, words):
        for word in words:
            self.add(word)

    def add(self, word):
        key =  self._key(word)
        words = self._words.get(key, [])
        words.append(word)
        self._words[key] = words
    
    def _key(self, word):
        return ''.join(sorted(word))

    def clear(self):
        self._words = {}
    
    def getBrother(self, word, index):
        key = self._key(word)
        words = sorted(self._words.get(key, []))
        i, cnt, fword = 1, 0, ''

        for w in words:
            if w == word:
                continue
            if i == index:
                fword = w
            cnt += 1
            i += 1
        return cnt, fword

def solution():
    _, *words, word, index = input().split()
    d = Dict()
    d.addWords(words)
    cnt, fword = d.getBrother(word, int(index))
    print(cnt)
    if fword != '':
        print(fword)

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception:
            break