# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/


class Solution:
    """1233. Remove Sub-Folders from the Filesystem

    Given a list of folders `folder`, return *the folders after removing all **sub-
    folders** in those folders*. You may return the answer in **any order**.

    If a `folder[i]` is located within another `folder[j]`, it is called a **sub-
    folder** of it. A sub-folder of `folder[j]` must start with `folder[j]`, followed by
    a `"/"`. For example, `"/a/b"` is a sub-folder of `"/a"`, but `"/b"` is not a sub-
    folder of `"/a/b/c"`.

    The format of a path is one or more concatenated strings of the form: `'/'` followed
    by one or more lowercase English letters.

    * For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an
    empty string and `"/"` are not."""

    def remove_subfolders(self, folder: list[str]) -> list[str]:
        # Check if the input list is empty, return empty list if true
        if not folder:
            return []
        # Sort the folder list to ensure parent folders come before sub-folders
        folder.sort()
        # Initialize result with the first folder (after sorting)
        result = [folder[0]]
        # Iterate through remaining folders to check for sub-folders
        for cur in folder[1:]:
            # Get the last folder added to the result
            last = result[-1]
            # Check if current folder is not a sub-folder of the last result folder
            if not cur.startswith(last + "/"):
                # Add current folder to result if it's not a sub-folder
                result.append(cur)
        # Return the list of folders with sub-folders removed
        return result

    removeSubfolders = remove_subfolders
