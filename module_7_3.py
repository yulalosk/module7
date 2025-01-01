class WordsFinder:
    res = {}
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):  #
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';',':','-']
        for fn in self.file_names:
            with open(fn, 'r',encoding='utf-8') as file:
                clear_line = file.read().lower()
                for symb in punctuation:
                    clear_line = clear_line.replace(symb, '')
                   # all_words = clear_line.split()
                    all_words[fn] = clear_line.split()
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            pos = 0
            if word.lower() in words:
                pos = words.index(word.lower()) + 1
                self.res[name] = pos
            return self.res

    def count(self, word):  
        for name, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[name] = counter
                return self.res



f = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(f)
print(WordsFinder.get_all_words(f))

finder1 = WordsFinder('Mother Goose - Mondays Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'), '\n')