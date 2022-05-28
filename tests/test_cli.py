from inspect import cleandoc

import pytest
from click.testing import CliRunner
from dirlisting.cli import app

from test_helper import assert_by_lines


def test_version():
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "app, version" in result.output


def test_file_input():
    input = cleandoc(
        """
        - toplevel:
          - subdir1:
            - file1.txt
          - subdir2:
            - file2.txt
            - file3.txt
        """
    )
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("input.yaml", "w") as f:
            f.write(input)

        result = runner.invoke(app, ["input.yaml"])
        assert result.exit_code == 0
        assert "toplevel" in result.output


@pytest.fixture
def unsorted():
    input = cleandoc(
        """
        - toplevel:
          - xdir:
            - bfile.txt
            - afile.txt
          - pfile.txt
          - mdir:
            - cfile.txt
            - dfile.txt
          - efile.txt
        """
    )
    return input


def test_sorted(unsorted):
    expected = """
        toplevel
        ├── efile.txt
        ├── mdir
        │   ├── cfile.txt
        │   └── dfile.txt
        ├── pfile.txt
        └── xdir
            ├── afile.txt
            └── bfile.txt
        """
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("input.yaml", "w") as f:
            f.write(unsorted)

        result = runner.invoke(app, ["--sort", "input.yaml"])
        assert result.exit_code == 0
        assert_by_lines(result.output, expected)


def test_dirsfirst(unsorted):
    expected = """
        toplevel
        ├── xdir
        │   ├── bfile.txt
        │   └── afile.txt
        ├── mdir
        │   ├── cfile.txt
        │   └── dfile.txt
        ├── pfile.txt
        └── efile.txt
        """
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("input.yaml", "w") as f:
            f.write(unsorted)

        result = runner.invoke(app, ["--dirsfirst", "input.yaml"])
        assert result.exit_code == 0
        assert_by_lines(result.output, expected)
