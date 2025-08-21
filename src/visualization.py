import matplotlib.pyplot as plt 


def separate_chars_and_frequencies(char_freq: dict) -> tuple[list, list]:
    
    """
    Separate the characters and their frequencies from a dictionary.

    Parameters:
        char_freq_dict (dict): Dictionary with characters as keys and frequencies as values.

    Returns:
        tuple[list, list]: A tuple containing two lists:
            - the list of characters
            - the list of frequencies
    """
    
    chars = []
    frequencies = []

    for char, freq in char_freq.items():
        chars.append(char)
        frequencies.append(freq)

    return chars, frequencies


def visualize_data(x: list, y: list) -> None:
    
    """
    Plot a simple line graph of x vs y using matplotlib.

    Parameters:
        x (list): List of x-axis values.
        y (list): List of y-axis values.

    Raises:
        TypeError: If `x` or `y` is not a list.
    """
    
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("Both 'x' and 'y' must be lists.")

    plt.bar(x, y)
    plt.title("Letter Frequencies")
    plt.xlabel("Characters")
    plt.ylabel("Frequencies")
    plt.savefig("letter_frequencies.png")
    plt.close()