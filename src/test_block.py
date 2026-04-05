import unittest

from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    # ---- HEADING ----
    def test_heading_single_hash(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING_1)

    def test_heading_multiple_hashes(self):
        self.assertEqual(block_to_block_type("###### Title"), BlockType.HEADING_6)

    def test_invalid_heading(self):
        self.assertEqual(block_to_block_type("####NoSpace"), BlockType.PARAGRAPH)

    # ---- CODE ----
    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_invalid_code_block(self):
        block = "```print('hi')```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # ---- QUOTE ----
    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> hello"), BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> line1\n> line2\n> line3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_invalid_quote(self):
        block = "> line1\nline2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # ---- UNORDERED LIST ----
    def test_unordered_list(self):
        block = "- item1\n- item2\n- item3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = "- item1\nitem2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # ---- ORDERED LIST ----
    def test_ordered_list(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_invalid_ordered_list_wrong_order(self):
        block = "1. one\n3. two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_ordered_list_no_space(self):
        block = "1.one\n2.two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # ---- PARAGRAPH ----
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just text."), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "This is line one.\nThis is line two."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)