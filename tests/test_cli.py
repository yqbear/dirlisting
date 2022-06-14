from inspect import cleandoc

import pytest
from click.testing import CliRunner
from dirlisting import __version__
from dirlisting.cli import app

from test_helper import assert_by_lines


def run_app(*params, runner=None):
    if runner is None:
        runner = CliRunner()
    result = runner.invoke(app, params)
    assert result.exit_code == 0
    return result.output.rstrip()


def test_version():
    assert run_app("--version") == f"app, version {__version__}"


@pytest.fixture
def runner_and_file():
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
    filename = "unsorted.yaml"
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open(filename, "w", encoding="utf-8") as yamlfile:
            yamlfile.write(input)
        yield runner, filename


def test_file_input(runner_and_file):
    runner, filename = runner_and_file
    assert "toplevel" in run_app(filename, runner=runner)


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


@pytest.mark.parametrize("opt", ["--sort", "-s"])
def test_sorted(opt, runner_and_file):
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
    runner, filename = runner_and_file
    assert_by_lines(run_app(opt, filename, runner=runner), expected)


@pytest.mark.parametrize("opt", ["--dirsfirst", "-d"])
def test_dirsfirst(opt, runner_and_file):
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
    runner, filename = runner_and_file
    assert_by_lines(run_app(opt, filename, runner=runner), expected)


@pytest.mark.parametrize("out_opt", ["--output", "-o"])
def test_file_output(out_opt, runner_and_file):
    expected = """
        toplevel
        ├── xdir
        │   ├── bfile.txt
        │   └── afile.txt
        ├── pfile.txt
        ├── mdir
        │   ├── cfile.txt
        │   └── dfile.txt
        └── efile.txt
        """
    runner, filename = runner_and_file
    run_app(out_opt, "listing.txt", filename, runner=runner)
    with open("listing.txt", "r", encoding="utf-8") as f:
        assert_by_lines(f.read(), expected)
