import os
import re

generic_types_pep_585 = [
    "Tuple",
    "List",
    "Dict",
    "Set",
    "FrozenSet",
    "Type",
]

for dir_ in ["202308", "202309", "202310", "202311"]:
    for root, _, files in os.walk(dir_):
        for file_ in files:
            if file_.endswith(".py"):
                with open(f"{root}/{file_}", "r") as fp:
                    content = fp.read()
                    for word in generic_types_pep_585:
                        # new_content = content.replace(word, word.lower())
                        content = re.sub(
                            f"""
                            (?:             # set our negative look behind choices to non-capture
                                (?<!\\# )   # negative look behid for line comments like '# Type'
                                |
                                (?<!\)\:)   # negative look behind for '):' in the case of redundant google-style docstrings
                            )               # end our negative look behind choices
                            ({word})        # our only capture group
                            (?:             # set our positive lookahead choices
                                (?=\\[)     # include when it's like 'Type[...].
                                |
                                (?=\\ ?of\\ ?)  # include when it's like 'List of List ...'
                            )
                            """,
                            word.lower(),
                            content,
                            flags=re.MULTILINE | re.VERBOSE,
                        )
                with open(f"{root}/{file_}", "w") as fp:
                    fp.write(content)
