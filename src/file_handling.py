def read_file(file_path: str) -> str:
    
    """
    Read a text file and return its content as a single string with newline characters removed.

    Parameters:
        file_path (str): Path to the file, absolute or relative.

    Returns:
        str: The file content as a string without newline characters,
             or an empty string if an error occurs.

    Raises:
        TypeError: If `file_path` is not a string.
    """

    if not isinstance(file_path, str):
        raise TypeError(f"Expected a string as parameter, got {type(file_path).__name__}")

    try:
        with open(file_path, "r") as f:
            text = f.read().replace("\n", "")
            return text
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    except Exception as e:
        print(f"An error occourred while reading the file {file_path}.")

    return ""