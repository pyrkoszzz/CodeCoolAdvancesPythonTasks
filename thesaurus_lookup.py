from PyDictionary import PyDictionary


class WordLookup:
    def __init__(self):
        self.dictionary = PyDictionary()

    def get_definition(self, word: str) -> dict | None:
        try:
            definition = self.dictionary.meaning(word)
            return definition
        except Exception as e:
            print(f"Error fetching definition: {e}")
            return None

    def get_synonyms(self, word: str) -> dict | list | None:
        try:
            synonyms = self.dictionary.synonym(word)
            return synonyms
        except Exception as e:
            print(f"Error fetching synonyms: {e}")
            return None


if __name__ == "__main__":
    word_lookup = WordLookup()

    try:
        word = input("Input word: ")

        definition = word_lookup.get_definition(word)
        if definition:
            print(f"\nDefinition of '{word}':")
            for part_of_speech, meanings in definition.items():
                print(f"{part_of_speech.capitalize()}: {', '.join(meanings)}")
        synonyms = word_lookup.get_synonyms(word)
        if synonyms:
            print(f"\nSynonyms of '{word}': {', '.join(synonyms)}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
