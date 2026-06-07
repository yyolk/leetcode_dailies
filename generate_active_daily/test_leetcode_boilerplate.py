import textwrap
import unittest

from generate_active_daily.leetcode_boilerplate import (
    extract_external_docstring_lines,
    select_python3_starter_code,
    strip_external_block_from_starter_code,
)


class TestLeetcodeBoilerplate(unittest.TestCase):
    def test_select_python3_from_code_snippets(self):
        question = {
            "codeSnippets": [
                {"langSlug": "python", "code": "python2"},
                {"langSlug": "python3", "code": "python3-from-snippet"},
            ],
            "codeDefinition": '[{"value": "python3", "defaultCode": "python3-from-definition"}]',
        }
        self.assertEqual("python3-from-snippet", select_python3_starter_code(question))

    def test_select_python3_falls_back_to_code_definition(self):
        question = {
            "codeSnippets": [],
            "codeDefinition": '[{"value": "python3", "defaultCode": "python3-from-definition"}]',
        }
        self.assertEqual(
            "python3-from-definition", select_python3_starter_code(question)
        )

    def test_select_python3_raises_when_missing(self):
        question = {
            "codeSnippets": [],
            "codeDefinition": '[{"value": "python", "defaultCode": "python2-only"}]',
        }
        with self.assertRaisesRegex(ValueError, "did not include python3 starter code"):
            select_python3_starter_code(question)

    def test_extract_external_docstring_lines(self):
        starter_code = textwrap.dedent(
            '''\
            """
            # Definition for a Node.
            class Node:
                def __init__(self, x: int):
                    self.val = int(x)
            """

            class Solution:
                def copyRandomList(self, head: "Node | None") -> "Node | None":
            '''
        )
        self.assertEqual(
            [
                "Definition for a Node.",
                "    class Node:",
                "        def __init__(self, x: int):",
                "            self.val = int(x)",
            ],
            extract_external_docstring_lines(starter_code),
        )

    def test_strip_external_block_from_starter_code(self):
        starter_code = textwrap.dedent(
            '''\
            """
            # Definition for a Node.
            """

            class Solution:
                def solve(self):
            '''
        )
        self.assertEqual(
            "class Solution:\n    def solve(self):",
            strip_external_block_from_starter_code(starter_code),
        )

    def test_extract_external_docstring_lines_heading_only(self):
        starter_code = textwrap.dedent(
            '''\
            """
            # Definition for a Node.
            """
            class Solution:
                def solve(self):
            '''
        )
        self.assertEqual(
            ["Definition for a Node."], extract_external_docstring_lines(starter_code)
        )


if __name__ == "__main__":
    unittest.main()
