#!/usr/bin/python3
"""
Import necessary modules
"""
import re
import os
import sys


def convert_markdown_to_html(md, html):
    """
    Converts a Markdown file to HTML.

    Args:
        md (str): Path to the input Markdown file.
        html (str): Path to the output HTML file.
    """
    if not (os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1])):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(sys.argv[1], encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(
                    f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write the HTML output to a file
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Check that the correct number of arguments were
    # provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)
    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(sys.argv[1], sys.argv[2])

    # Exit with a successful status code
    sys.exit(0)
