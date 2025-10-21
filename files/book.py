from pathlib import Path

def count_words(book):
    try:
        book = Path(f'{book}.txt')
        contents = book.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("We coulndt find the funcking book")
    else: 
        words = contents.split()
        length = len(words)
        print(f'The book "{book}" has {length} words')

count_words('How to Live on 24 Hours a Day by Arnold Bennett')
count_words('Moby Dick; Or, The Whale by Herman Melville')

def count_phrase(book, phrase):
    try:
        book = Path(f'{book}.txt')
        contents = book.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("We coulndt find the funcking book")
    else: 
        words = contents.split()
        length = len(words)
        print(f'The book "{book}" has {length} words')

        phrase_count = contents.count(f'{phrase.lower()}')
        print(f'The book "{book}" has the phrase "{phrase}" {phrase_count} times')

count_phrase('Moby Dick; Or, The Whale by Herman Melville', 'then')