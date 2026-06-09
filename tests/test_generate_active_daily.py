"""Tests for generate_active_daily.utils module."""

import ast
import textwrap
import pytest


from generate_active_daily.leetcode_boilerplate import (
    extract_external_docstring_lines,
    select_python3_starter_code,
    strip_external_block_from_starter_code,
)
from generate_active_daily.backfill_remove_docstring_type_annotations import (
    update_docstrings_in_source,
)
from generate_active_daily.utils import (
    camel_to_snake,
    extract_constraints_lines,
    modify_class_docstring,
    remove_redundant_google_docstring_types,
    wrap_docstring,
    write_file,
)


class TestCamelToSnake:
    def test_simple_camel_case(self):
        assert camel_to_snake("twoSum") == "two_sum"

    def test_longer_camel_case(self):
        assert camel_to_snake("myProblemSolution") == "my_problem_solution"

    def test_already_lowercase(self):
        assert camel_to_snake("lowercase") == "lowercase"

    def test_single_word(self):
        assert camel_to_snake("word") == "word"

    def test_leading_uppercase_stripped(self):
        # Leading underscore should be removed then lowercased
        assert camel_to_snake("IsValid") == "is_valid"

    def test_is_valid(self):
        assert camel_to_snake("isValid") == "is_valid"

    def test_multiple_consecutive_uppercase(self):
        # Each uppercase letter gets a preceding underscore
        assert camel_to_snake("parseHTML") == "parse_h_t_m_l"

    def test_single_uppercase_letter(self):
        assert camel_to_snake("A") == "a"

    def test_leetcode_common_name(self):
        assert camel_to_snake("maxProfit") == "max_profit"

    def test_three_part_name(self):
        assert camel_to_snake("findMedianSortedArrays") == "find_median_sorted_arrays"


class TestExtractConstraintsLines:
    def test_extracts_constraints_heading_and_bullets(self):
        html = """\
<div>
    <p>Description text.</p>
    <p><strong>Constraints:</strong></p>
    <ul>
        <li>1 &lt;= nums.length &lt;= 1000</li>
        <li>-10^4 &lt;= nums[i] &lt;= 10^4</li>
    </ul>
</div>
"""
        assert extract_constraints_lines(html) == [
            "Constraints:",
            "* 1 <= nums.length <= 1000",
            "* -10^4 <= nums[i] <= 10^4",
        ]

    def test_returns_empty_when_constraints_absent(self):
        html = "<div><p>No constraints section here.</p></div>"
        assert extract_constraints_lines(html) == []


class TestWrapDocstring:
    def test_empty_list(self):
        result = wrap_docstring([])
        assert result == ""

    def test_single_short_line(self):
        result = wrap_docstring(["Short line"])
        assert result == "Short line"

    def test_single_long_line_is_wrapped(self):
        long_line = "A" * 50 + " " + "B" * 50
        result = wrap_docstring([long_line])
        # Should be wrapped at TEXT_WIDTH (88)
        for line in result.splitlines():
            assert len(line) <= 88

    def test_multiple_lines_separated_by_blank(self):
        result = wrap_docstring(["First line", "Second line"])
        assert "First line" in result
        assert "Second line" in result
        # Lines should be separated by a blank line
        assert "\n\n" in result

    def test_indentation_reduces_width(self):
        long_line = "word " * 20  # ~100 chars
        result_no_indent = wrap_docstring([long_line], indentation=0)
        result_with_indent = wrap_docstring([long_line], indentation=20)
        # With indentation, lines should be shorter
        max_no_indent = max(len(l) for l in result_no_indent.splitlines())
        max_with_indent = max(len(l) for l in result_with_indent.splitlines())
        assert max_with_indent <= max_no_indent

    def test_three_lines(self):
        result = wrap_docstring(["Line 1", "Line 2", "Line 3"])
        assert result.count("\n\n") == 2


class TestModifyClassDocstring:
    """Tests for the AST-based class docstring modifier."""

    SIMPLE_CODE = """\
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ...
"""

    def test_renames_method_to_snake_case(self):
        result = modify_class_docstring(
            self.SIMPLE_CODE, ["Two sum description"], "1. Two Sum\n"
        )
        tree = ast.parse(result)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                assert node.name == "two_sum"

    def test_adds_camel_alias(self):
        result = modify_class_docstring(
            self.SIMPLE_CODE, ["Two sum description"], "1. Two Sum\n"
        )
        assert "twoSum = two_sum" in result

    def test_inserts_docstring(self):
        result = modify_class_docstring(
            self.SIMPLE_CODE, ["Two sum description"], "1. Two Sum\n"
        )
        assert "Two sum description" in result

    def test_renames_camel_case_args(self):
        code = """\
class Solution:
    def maxProfit(self, pricesList: list[int]) -> int:
        ...
"""
        result = modify_class_docstring(code, ["Max profit"], "122. Best Time to Buy\n")
        tree = ast.parse(result)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "max_profit":
                for arg in node.args.args:
                    if arg.arg != "self":
                        assert arg.arg == "prices_list"

    def test_lowercases_list_annotation(self):
        code = """\
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
"""
        result = modify_class_docstring(code, ["description"], "1. Title\n")
        # List should be lowercased to list
        assert "List[" not in result

    def test_lowercases_dict_annotation(self):
        code = """\
class Solution:
    def groupAnagrams(self, strs: List[str]) -> Dict[str, List[str]]:
        ...
"""
        result = modify_class_docstring(code, ["description"], "49. Group Anagrams\n")
        assert "Dict[" not in result
        assert "List[" not in result

    def test_existing_docstring_replaced(self):
        code = '''\
class Solution:
    """Old docstring."""
    def solve(self, x: int) -> int:
        ...
'''
        result = modify_class_docstring(code, ["New docstring content"], "1. Title\n")
        # Old docstring should be replaced
        assert "Old docstring." not in result

    def test_returns_valid_python(self):
        result = modify_class_docstring(
            self.SIMPLE_CODE, ["Description line"], "1. Two Sum\n"
        )
        # Should parse without errors
        ast.parse(result)

    def test_skips_dunder_and_handles_missing_return_annotation(self):
        code = """\
class Solution:
    def __init__(self, values):
        self.values = values

    def twoSum(self, nums, target):
        ...
"""
        result = modify_class_docstring(code, ["Description"], "1. Two Sum\n")
        assert "def __init__(self, values):" in result
        assert "def two_sum(self, nums, target):" in result
        assert "twoSum = two_sum" in result
        ast.parse(result)

    def test_no_alias_added_when_only_dunder_methods_exist(self):
        code = """\
class Solution:
    def __init__(self, value):
        self.value = value
"""
        result = modify_class_docstring(code, ["Description"], "1. Title\n")
        assert "def __init__(self, value):" in result
        tree = ast.parse(result)
        solution_node = next(
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef) and node.name == "Solution"
        )
        assert not any(
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) for target in node.targets)
            for node in solution_node.body
        )

    def test_strips_redundant_types_from_method_docstring(self):
        code = '''\
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Args:
            nums (list[int]): Input nums.
            target (int): Target value.

        Returns:
            list[int]: A pair of indexes.
        """
        ...
'''
        result = modify_class_docstring(code, ["Description"], "1. Title\n")
        assert "nums (list[int]):" not in result
        assert "target (int):" not in result
        assert "list[int]: A pair of indexes." not in result
        assert "nums: Input nums." in result
        assert "target: Target value." in result
        assert "A pair of indexes." in result


class TestRemoveRedundantGoogleDocstringTypes:
    def test_strips_arg_and_return_types(self):
        docstring = """Args:
    arr (list[int]): Input.
    target (int): Desired value.

Returns:
    bool: Whether a pair exists.
"""
        assert (
            remove_redundant_google_docstring_types(docstring)
            == """Args:
    arr: Input.
    target: Desired value.

Returns:
    Whether a pair exists.
"""
        )

    def test_keeps_already_untyped_sections_unchanged(self):
        docstring = """Args:
    arr: Input.

Returns:
    Whether a pair exists.
"""
        assert remove_redundant_google_docstring_types(docstring) == docstring

    def test_does_not_modify_non_target_sections(self):
        docstring = """Raises:
    ValueError: On bad input.
"""
        assert remove_redundant_google_docstring_types(docstring) == docstring


class TestBackfillRemoveDocstringTypeAnnotations:
    def test_updates_only_docstring_sections(self):
        source = '''\
class Solution:
    """Args:
    nums (list[int]): class-level docs.
    """

    def solve(self):
        """
        Args:
            nums (list[int]): Input nums.
        Returns:
            list[int]: Output values.
        """
        data = "Args:\\n    nums (list[int]): should stay unchanged"
        return data
'''
        result = update_docstrings_in_source(source)
        assert "nums: class-level docs." in result
        assert "nums: Input nums." in result
        assert "Output values." in result
        assert 'data = "Args:\\n    nums (list[int]): should stay unchanged"' in result


class TestWriteFile:
    def test_creates_file(self, tmp_path):
        write_file(tmp_path, "test.py", "content")
        assert (tmp_path / "test.py").read_text() == "content"

    def test_creates_directory_if_not_exists(self, tmp_path):
        new_dir = tmp_path / "new" / "nested"
        write_file(new_dir, "test.py", "hello")
        assert (new_dir / "test.py").exists()

    def test_raises_file_exists_error_when_exists_no_overwrite(self, tmp_path):
        (tmp_path / "existing.py").write_text("original")
        with pytest.raises(FileExistsError):
            write_file(tmp_path, "existing.py", "new content")

    def test_original_preserved_when_no_overwrite(self, tmp_path):
        (tmp_path / "existing.py").write_text("original")
        with pytest.raises(FileExistsError):
            write_file(tmp_path, "existing.py", "new content")
        assert (tmp_path / "existing.py").read_text() == "original"

    def test_overwrites_when_flag_set(self, tmp_path):
        (tmp_path / "existing.py").write_text("original")
        write_file(tmp_path, "existing.py", "new content", overwrite=True)
        assert (tmp_path / "existing.py").read_text() == "new content"

    def test_writes_empty_content(self, tmp_path):
        write_file(tmp_path, "empty.py", "")
        assert (tmp_path / "empty.py").read_text() == ""


class TestLeetcodeBoilerplate:
    def test_select_python3_from_code_snippets(self):
        question = {
            "codeSnippets": [
                {"langSlug": "python", "code": "python2"},
                {"langSlug": "python3", "code": "python3-from-snippet"},
            ],
            "codeDefinition": '[{"value": "python3", "defaultCode": "python3-from-definition"}]',
        }
        assert select_python3_starter_code(question) == "python3-from-snippet"

    def test_select_python3_falls_back_to_code_definition(self):
        question = {
            "codeSnippets": [],
            "codeDefinition": '[{"value": "python3", "defaultCode": "python3-from-definition"}]',
        }
        assert select_python3_starter_code(question) == "python3-from-definition"

    def test_select_python3_raises_when_missing(self):
        question = {
            "codeSnippets": [],
            "codeDefinition": '[{"value": "python", "defaultCode": "python2-only"}]',
        }
        with pytest.raises(ValueError, match="did not include python3 starter code"):
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
        assert extract_external_docstring_lines(starter_code) == [
            "Definition for a Node.",
            "    class Node:",
            "        def __init__(self, x: int):",
            "            self.val = int(x)",
        ]

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
        assert strip_external_block_from_starter_code(starter_code) == (
            "class Solution:\n    def solve(self):"
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
        assert extract_external_docstring_lines(starter_code) == [
            "Definition for a Node."
        ]
