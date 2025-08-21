def clean_txt(text: str) -> str:

    """
    Clean a string by removing all non-alphabetic characters and converting
    the remaining characters to lowercase.

    Parameters:
        text (str): Input string to clean.

    Returns:
        str: A lowercase string containing only alphabetic characters.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError(f"Expected a string for 'text', got {type(text).__name__}.")

    return "".join(char.lower() for char in text if char.isalpha())


def count_letters(text: str) -> dict:

    """
    Count the frequency of each character in a string.

    Parameters:
        text (str): Input string to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.

    Raises:
        TypeError: If `text` is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError(f"Expected a string for 'text', got {type(text).__name__}.")
    letter_frequencies = dict()

    for char in text:
        letter_frequencies[char] = letter_frequencies.get(char, 0) + 1
    
    return letter_frequencies