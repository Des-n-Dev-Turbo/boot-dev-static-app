from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    HEADING_4 = "heading_4"
    HEADING_5 = "heading_5"
    HEADING_6 = "heading_6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # ---- HEADING ----
    if re.match(r"^#{1,6} .+", block):
        # Determine the heading level based on the number of hashes
        heading_level = len(re.match(r"^#{1,6}", block).group())
        if heading_level == 1:
            return BlockType.HEADING_1
        elif heading_level == 2:
            return BlockType.HEADING_2
        elif heading_level == 3:
            return BlockType.HEADING_3
        elif heading_level == 4:
            return BlockType.HEADING_4
        elif heading_level == 5:
            return BlockType.HEADING_5
        elif heading_level == 6:
            return BlockType.HEADING_6

    # ---- CODE BLOCK ----
    if block.startswith("```") and block.endswith("```"):
        # Must be multiline: ```\n...\n```
        if len(lines) >= 2 and lines[0] == "```" and lines[-1] == "```":
            return BlockType.CODE

    # ---- QUOTE BLOCK ----
    if all(re.match(r"^> ?.*", line) for line in lines):
        return BlockType.QUOTE

    # ---- UNORDERED LIST ----
    if all(re.match(r"^- .+", line) for line in lines):
        return BlockType.UNORDERED_LIST

    # ---- ORDERED LIST ----
    is_ordered = True
    for i, line in enumerate(lines):
        expected = f"{i+1}. "
        if not line.startswith(expected):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    # ---- DEFAULT ----
    return BlockType.PARAGRAPH