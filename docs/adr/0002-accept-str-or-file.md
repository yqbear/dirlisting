# 2. Accept str or file

Date: 2022-05-25

## Status

Accepted

## Context

A decision has to be made on what is passed in to the directory listing object. It could
be the filename for a file containing YAML, a stream, or a YAML string. The choice
determines how smart the object has to be about the input. The result should be a data
structure produced from the input.

## Decision

The decision is to allow file streams or strings. The eventual CLI can easily open a
file from a filename and pass it in and a line or piped in string can also be handled.

## Consequences

This adds a little more complexity to the construtor for the object but nothing major.
At the moment, I'm not thinking directly about unicode strings but this is something
that should be checked later.
