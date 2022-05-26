from inspect import cleandoc

from click.testing import CliRunner
from dirlisting.cli import app


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
