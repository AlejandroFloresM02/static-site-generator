import unittest

from getcontent import extract_title


class TestGetContent(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Title of the Document"
        self.assertEqual(extract_title(markdown), "Title of the Document")

    def test_extract_title_with_spaces(self):
        markdown = "# Title of the Document with Spaces"
        self.assertEqual(extract_title(markdown), "Title of the Document with Spaces")

    def test_extract_title_with_multiple_hashes(self):
        markdown = "## Title of the Document with Multiple Hashes"
        self.assertEqual(
            extract_title(markdown), "Title of the Document with Multiple Hashes"
        )
