# dirlisting

Create a directory tree listing diagram from a text file.

## Installation

```bash
$ pip install dirlisting
```

## Usage

`dirlisting` can be used to create a directory tree digram that looks like those created
with the `tree` command, but from a text file instead of walking an actual directory
tree.

### From code

```python
from dirlisting.dirlisting import Dirlisting
with open("input.yaml") as f:
    listing = Dirlisting(f)
listing.print()
```

### From the command line

just use `dirlisting <filename>`.

### File format

The input file is a [yaml](https://yaml.org/) file. The contents of a directory are
sequences, files are final strings (`- filename`), and directories are mappings (`-
dirname:`). A listing would look like the following.

:::::{grid} 2
::::{grid-item-card} YAML File
```yaml
- topdir:
  - subdir1:
  - file1.txt
  - file2.txt
  - subdir2:
    - file3.txt
```
::::
::::{grid-item-card} Output
```
topdir
├── emptydir
├── file1.txt
├── file2.txt
└── subdir
    └── file3.txt
```
::::
:::::

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this
project is released with a Code of Conduct. By contributing to this project, you agree
to abide by its terms.

## License

`dirlisting` was created by Stephan Poole. It is licensed under the terms of the MIT
license.

## Credits

`dirlisting` was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the
`py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
