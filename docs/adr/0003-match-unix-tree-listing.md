# 3. Match unix tree listing

Date: 2022-05-25

## Status

Accepted

## Context

There are a number of different formats for the output. The output can use ascii
graphical type characters or be tied to standard alphanumerics. There is also a
difference between the `tree` command used in *nix and the `tree` command in Windows.

### Output from *nix

```
top_level
├── subdir_01
│   ├── file_01_a.txt
│   ├── file_01_b.txt
│   └── subsubdir_01_01
│       ├── file_01_01_a.txt
│       └── file_01_01_b.txt
├── subdir_02
│   ├── subsubdir_02_01
│   └── subsubdir_02_02
└── subdir_03
    ├── file_03_a.txt
    ├── file_03_b.txt
    └── subsubdir_03_01
        └── file_03_01_a.txt
```

### Output from Windows

```
TOP_LEVEL
├───subdir_01
│   │   file_01_a.txt
│   │   file_01_b.txt
│   │
│   └───subsubdir_01_01
│           file_01_01_a.txt
│           file_01_01_b.txt
│
├───subdir_02
│   ├───subsubdir_02_01
│   └───subsubdir_02_02
└───subdir_03
    │   file_03_a.txt
    │   file_03_b.txt
    │
    └───subsubdir_03_01
            file_03_01_a.txt
```

## Decision

The decision is to use the *nix format. This is equivalent to running `tree --noreport
<dirname>`. For documentation, the extra blank lines of the Windows output would use up
valuable space without contributing much to readability.

## Consequences

The directory listing is more compact but still easy to read. The files have graphic
lines leading to them in the *nix format that are not present in the Windows format.
This is actually easier since all children of a directory (dir or file) are treated the
same in regards to lead-in characters.
