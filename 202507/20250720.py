# https://leetcode.com/problems/delete-duplicate-folders-in-system/
from collections import defaultdict


class Node:
    def __init__(self):
        self.children = {}
        self.sig = None


class Solution:
    """1948. Delete Duplicate Folders in System

    Due to a bug, there are many duplicate folders in a file system. You are given a 2D
    array `paths`, where `paths[i]` is an array representing an absolute path to the
    `ith` folder in the file system.

    * For example, `["one", "two", "three"]` represents the path `"/one/two/three"`.

    Two folders (not necessarily on the same level) are **identical** if they contain
    the **same non-empty** set of identical subfolders and underlying subfolder
    structure. The folders **do not** need to be at the root level to be identical. If
    two or more folders are **identical**, then **mark** the folders as well as all
    their subfolders.

    * For example, folders `"/a"` and `"/b"` in the file structure below are identical.
    They (as well as their subfolders) should **all** be marked:

      + `/a`

      + `/a/x`

      + `/a/x/y`

      + `/a/z`

      + `/b`

      + `/b/x`

      + `/b/x/y`

      + `/b/z`

    * However, if the file structure also included the path `"/b/w"`, then the folders
    `"/a"` and `"/b"` would not be identical. Note that `"/a/x"` and `"/b/x"` would
    still be considered identical even with the added folder.

    Once all the identical folders and their subfolders have been marked, the file
    system will **delete** all of them. The file system only runs the deletion once, so
    any folders that become identical after the initial deletion are not deleted.

    Return *the 2D array* `ans` *containing the paths of the **remaining** folders after
    deleting all the marked folders. The paths may be returned in **any** order*."""

    def delete_duplicate_folder(self, paths: list[list[str]]) -> list[list[str]]:
        # Create the root node of the file system tree
        root = Node()
        # Build the tree by iterating through each path
        for path in paths:
            # Start at the root for each path
            cur = root
            # Process each folder in the path
            for folder in path:
                # Create a new node if the folder doesn't exist
                if folder not in cur.children:
                    cur.children[folder] = Node()
                # Move to the child node
                cur = cur.children[folder]

        # Initialize a defaultdict to count folder signatures
        sig_to_count = defaultdict(int)

        # Define a function to build a signature for each node
        def build_sig(node):
            # List to store child folder signatures
            child_entries = []
            # Iterate through children in sorted order
            for name in sorted(node.children):
                # Recursively build signature for child node
                child_sig = build_sig(node.children[name])
                # Add child name and signature as a tuple
                child_entries.append((name, child_sig))
            # Create a tuple of child entries as the node's signature
            sig = tuple(child_entries)
            # Assign the signature to the node
            node.sig = sig
            # Increment count for non-empty folder signatures
            if node.children:
                sig_to_count[sig] += 1
            # Return the node's signature
            return sig

        # Build signatures starting from the root
        build_sig(root)

        # Initialize a set to store signatures of duplicate folders
        bad_sigs = set()
        # Identify signatures that appear multiple times
        for sig, cnt in sig_to_count.items():
            # Add signatures with count >= 2 to bad_sigs
            if cnt >= 2:
                bad_sigs.add(sig)

        # Initialize a list to store remaining paths
        result = []

        # Define a function to collect non-duplicate paths
        def collect(node, path):
            # Iterate through children in sorted order
            for name in sorted(node.children):
                # Get the child node
                child = node.children[name]
                # Skip if the child's signature is a duplicate
                if child.sig in bad_sigs:
                    continue
                # Create a new path by adding the current folder
                new_path = path + [name]
                # Add the new path to the result
                result.append(new_path)
                # Recursively collect paths from the child node
                collect(child, new_path)

        # Start collecting paths from the root
        collect(root, [])
        # Return the list of remaining paths
        return result

    deleteDuplicateFolder = delete_duplicate_folder
