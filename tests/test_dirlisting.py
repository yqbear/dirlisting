from io import StringIO

import pytest
from dirlisting import dirlisting

from test_helper import assert_by_lines


def test_single_dir_with_str(capsys):
    input = "- top:"
    listing = dirlisting.Dirlisting(input)
    listing.print()
    captured = capsys.readouterr()
    assert captured.out.startswith("top")


def test_single_dir_with_file(capsys):
    with StringIO("- toplevel:") as input:
        listing = dirlisting.Dirlisting(input)
    listing.print()
    captured = capsys.readouterr()
    assert captured.out.startswith("toplevel")


def test_child_files(capsys):
    input = """
        - top:
          - file1.txt
          - file2.txt
        """
    expected = """
        top
        ├── file1.txt
        └── file2.txt
        """
    listing = dirlisting.Dirlisting(input)
    listing.print()
    captured = capsys.readouterr()
    assert_by_lines(captured.out, expected)


def test_dir_as_child(capsys):
    input = """
        - top:
          - file1.txt
          - file2.txt
          - subdir:
            - file3.txt
        """
    expected = """
        top
        ├── file1.txt
        ├── file2.txt
        └── subdir
            └── file3.txt
        """
    listing = dirlisting.Dirlisting(input)
    listing.print()
    captured = capsys.readouterr()
    assert_by_lines(captured.out, expected)


def test_continue_past_subdir(capsys):
    input = """
        - toplevel:
          - subdir1:
            - file1.txt
            - file2.txt
          - subdir2:
            - file3.txt
            - file4.txt
        """
    expected = """
        toplevel
        ├── subdir1
        │   ├── file1.txt
        │   └── file2.txt
        └── subdir2
            ├── file3.txt
            └── file4.txt
        """
    listing = dirlisting.Dirlisting(input)
    listing.print()
    captured = capsys.readouterr()
    assert_by_lines(captured.out, expected)


@pytest.fixture
def unsorted():
    input = """
        - toplevel:
          - yfile.txt
          - mdir:
            - dfile.txt
            - bfile.txt
          - kdir:
            - afile.txt
          - bfile.txt
        """
    return input


def test_sorting_list(capsys, unsorted):
    expected = """
        toplevel
        ├── bfile.txt
        ├── kdir
        │   └── afile.txt
        ├── mdir
        │   ├── bfile.txt
        │   └── dfile.txt
        └── yfile.txt
        """
    listing = dirlisting.Dirlisting(unsorted)
    listing.print(is_sort=True)
    captured = capsys.readouterr()
    assert_by_lines(captured.out, expected)
