# 1. Use YAML for input

Date: 2022-05-25

## Status

Accepted

## Context

An input file is needed to create the directory listing. YAML provides a simple text
format that can be used and is easily converted to native data types for processing.

## Decision

Use YAML as the input format for the directory listing. Contents of a directory will be
sequences, files are final strings (`- filename`), and directories are mappings (`-
dirname:`). A listing would look like the following.

```
- toplevel:
  - afile.txt
  - directory:
    - bfile.txt
    - cfile.txt
  - lateralphabeticalfile.txt
```

## Consequences

Using YAML makes it easy to load the file into native data structures with one command.
The rest of the program can focus on how to parse the structure and output the directory
listing. The downside is that the user has to conform to a format and care must be taken
to match the ordering the user wants.
