class Solution:
    """68. Text Justification
    Given an array of strings words and a width maxWidth, 
    format the text such that each line has exactly maxWidth
    characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is,
    pack as many words as you can in each line.
    Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible.
    If the number of spaces on a line does not divide evenly between words,
    the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space is inserted between words.

    Note:
        - A word is defined as a character sequence consisting of non-space characters only.
        - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
        - The input array words contains at least one word.
    """
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        """Full justify text like a book in ascii sorta

        Args:
            words (List of str): A list of words that should be used to form the justified text
            max_width (int): The maximum width the text can take up, this also needs to be 
                the total size of the text that is taken up on most lines

        Returns:
            List of str: the completed, justified text. Returned as separate lines in a list.
        """
        lines = []
        current_line = []
        for word in words:
            if sum(len(w) for w in current_line) + len(current_line) + len(word) <= max_width:
                current_line.append(word)
            else:
                lines.append(current_line)
                current_line = [word]
        lines.append(current_line)

        justified_lines = []

        for idx, line in enumerate(lines):
            total_spaces = max_width - sum(len(word) for word in line)
            spaces_needed = len(line) - 1
            if idx == len(lines) - 1 or spaces_needed == 0:
                # Our line doesn't need any extra spaces, but we need to make sure to fill the rest
                justified_line = " ".join(line).ljust(max_width)
            else:
                spaces_between_words = total_spaces // spaces_needed
                extra_spaces = total_spaces % spaces_needed
                # Store the first word and create our new justified_line
                justified_line = line[0]
                for i in range(1, len(line)):
                    spaces = spaces_between_words
                    if i <= extra_spaces:
                        spaces += 1
                    justified_line += " " * spaces + line[i]
                
            justified_lines.append(justified_line)

        return justified_lines