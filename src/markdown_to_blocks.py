import textwrap


def markdown_to_blocks(markdown):
    normalized_markdown = textwrap.dedent(markdown).strip()
    if not normalized_markdown:
        return []

    split_markdown = normalized_markdown.split("\n\n")

    blocks = []
    for block in split_markdown:
        sanitized_block = block.strip()

        if sanitized_block:
            blocks.append(sanitized_block)

    return blocks