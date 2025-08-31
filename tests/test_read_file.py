import pytest

from src.file_handling import read_file


def test_read_file_success(tmp_path):

    file = tmp_path / "test.txt"
    file.write_text("Hello\nworld")

    result = read_file(str(file))
    assert result == "Helloworld"


def test_read_file_empty(tmp_path):

    file = tmp_path / "empty.txt"
    file.write_text("")
    
    result = read_file(str(file))
    assert result == ""


def test_read_file_not_a_string():

    with pytest.raises(TypeError):
        read_file(123)


if __name__ == "__main__":
    pytest.main()