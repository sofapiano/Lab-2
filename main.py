import json
import csv

DATASET_PATH = 'books-en.csv'
OUT_PATH = 'out.json'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res


def filter_year(dataset, title, year):
    filtered = []

    for line in dataset:
        obj = get_object(line, title)
        year_value = obj['Year-Of-Publication']
        if year_value == str(year):
            filtered.append(obj)

    dataset.seek(0)
    return filtered


def filter_book_title(dataset, title):
    ans = 0

    for line in dataset:
        obj = get_object(line, title)
        book_title_value = obj['Book-Title']
        if len(book_title_value) > 30:
            ans += 1

    dataset.seek(0)
    return ans


def find_by_author_filtered(dataset, title, author):
    
    results = []
    
    for line in dataset:
        obj = get_object(line, title)
        author_value = obj['Book-Author']
        if author_value == author:
            if int(obj['Year-Of-Publication']) >= 2018:
                results.append(obj)

    dataset.seek(0)
    return results


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:

        # название длиннее 30 символов
        title = get_title(dataset)
        print(filter_book_title(dataset, title))

        # поиск книги по автору (от 2018)
        print(find_by_author_filtered(dataset, title, input()))
        # но эта функция априори не может работать, т.к. в датасете нет книг после 2018 года