from inspect import cleandoc

from click.testing import CliRunner
from dirlisting.cli import app

from test_helper import assert_by_lines


def test_version():
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
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
        assert "toplevel" in result.output


def test_sorted():
    input = cleandoc(
        """
        - toplevel:
          - xdir:
            - bfile.txt
            - afile.txt
          - mdir:
            - cfile.txt
            - dfile.txt
        """
    )
    expected = """
        toplevel
        ├── mdir
        │   ├── cfile.txt
        │   └── dfile.txt
        └── xdir
            ├── afile.txt
            └── bfile.txt
        """
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("input.yaml", "w") as f:
            f.write(input)

        result = runner.invoke(app, ["--sort", "input.yaml"])
        assert_by_lines(result.output, expected)
