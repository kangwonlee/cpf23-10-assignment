import pathlib
import sys

import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import ex08


def test_a_z():
    result = ex08.func08('a', 'z')
    expected = 'abcdefghijklmnopqrstuvwxy'

    assert result == expected


def test_z_a():
    result = ex08.func08('z', 'a')
    expected = 'abcdefghijklmnopqrstuvwxy'

    assert result == expected


def test_A_Z():
    result = ex08.func08('A', 'Z')
    expected = 'abcdefghijklmnopqrstuvwxy'.upper()

    assert result == expected


def test_z_a():
    result = ex08.func08('Z', 'A')
    expected = 'abcdefghijklmnopqrstuvwxy'.upper()

    assert result == expected


if "__main__" == __name__:
    pytest.main([__file__])
