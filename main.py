import json
import os
import random

import openai


openai.api_key = os.environ['OPENAI_API_KEY']


def get_text_from_book():
    # Choose a random book.
    with open('books.json', 'r') as books_file:
        books = json.load(books_file)
        random_book = random.choice(books)
        random_file = random.choice(random_book['files'])

        # Choose a random starting point in the book.
        with open(os.path.join(random_book["local_path"], random_file), 'r') as book_text_file:
            total_lines = 0
            for line in book_text_file:
                total_lines += 1

            start_line = random.randint(1, total_lines - 100)  # -100 is just a shortcut to avoid EOF

        # Read a block of text and return it.
        # Closing and re-opening a file is faster than seeking to 0 in case of large files.
        with open(os.path.join(random_book['local_path'], random_file), 'r') as book_text_file:
            this_line = 0
            for line in book_text_file:
                this_line += 1
                if this_line < start_line:
                    continue
                if line.strip() == '':  # empty line denotes paragraph boundry
                    break

            length_threshold = 1200
            hard_length_limit = 3000
            raw_text = ''
            for line in book_text_file:
                raw_text = f'{raw_text} {line.strip()}'.strip()
                # Break at paragraphs to have the prompt generated at the later be more cohesive.
                if len(raw_text) >= length_threshold and line.strip() == '':
                    break

            return raw_text


def generate_scene_prompt(text_from_book):
    prompt_prefix = 'Describe this scene from a book to a painter so they can paint it:\n\n'
    completion = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'{prompt_prefix}{text_from_book}',
        max_tokens=256,
    )
    return completion['choices'][0]['text'].strip()


def generate_images_for_prompt(prompt):
    image = openai.Image.create(
        prompt=prompt,
        n=1,
        size='1024x1024',
    )
    return image['data'][0]['url']
