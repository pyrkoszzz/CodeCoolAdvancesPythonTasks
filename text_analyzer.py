import string


class TextAnalyzer:
    def __init__(self, file_path: str):
        try:
            with open(file_path, "r") as file:
                self.file_content = file.read().split()
                self.file_content_stripped = []
            for word in self.file_content:
                self.file_content_stripped.append(word.strip(string.punctuation).lower())
        except Exception as e:
            raise Exception(e)

    def word_count(self) -> int:
        return len(self.file_content)

    def sentence_count(self) -> int:
        sentence_counter = 0
        for word in self.file_content:
            if '.' in word or '!' in word or '?' in word:
                sentence_counter += 1
        return sentence_counter

    def avg_word_length(self) -> float:
        letters_count = [len(word) for word in self.file_content_stripped]
        return sum(letters_count) / len(self.file_content_stripped)

    def most_common_words(self, limit: int) -> list[tuple]:
        words_distinct = set(self.file_content_stripped)
        word_freq = dict(zip(words_distinct, [0] * len(words_distinct)))
        for word in word_freq.keys():
            word_freq[word] = self.file_content_stripped.count(word)
        word_freq_sorted = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
        return list(word_freq_sorted.items())[:limit]

    def most_common_words_better(self, limit: int) -> list[tuple]:
        word_freq = dict()
        for word in self.file_content_stripped:
            if word not in word_freq:
                word_freq[word] = self.file_content_stripped.count(word)
        word_freq_sorted = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        return word_freq_sorted[:limit]


if __name__ == '__main__':
    try:
        analyzer = TextAnalyzer('sample1.txt')
        print(analyzer.word_count())
        print(f'{analyzer.avg_word_length()}')
        print(analyzer.most_common_words(5))
        print(analyzer.most_common_words_better(5))
        print(analyzer.sentence_count())
    except Exception as e:
        print(f'Error occurred: {e}')
