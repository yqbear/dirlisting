from inspect import cleandoc


def assert_by_lines(output, expected):
    """Test the captured output against the expected output line-by-line.

    The expected output in
    """
    output_lines = output.splitlines()
    expected_lines = cleandoc(expected).splitlines()
    assert len(output_lines) == len(expected_lines)
    for index, line in enumerate(output_lines):
        assert line == expected_lines[index]
