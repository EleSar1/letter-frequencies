from .file_handling import read_file
from .processing import clean_txt, count_letters
from .visualization import separate_chars_and_frequencies, visualize_data


def main():
    
    text = read_file("files/sample.txt")
    cleaned = clean_txt(text)
    letter_frequencies = count_letters(cleaned)
    x, y = separate_chars_and_frequencies(letter_frequencies)

    visualize_data(x, y)