class Spreadsheet:
    """3797. Design Spreadsheet

    A spreadsheet is a grid with 26 columns (labeled from `'A'` to `'Z'`) and a given
    number of `rows`. Each cell in the spreadsheet can hold an integer value between 0
    and 105.

    Implement the `Spreadsheet` class:

    * `Spreadsheet(int rows)` Initializes a spreadsheet with 26 columns (labeled `'A'`
    to `'Z'`) and the specified number of rows. All cells are initially set to 0.

    * `void setCell(String cell, int value)` Sets the value of the specified `cell`. The
    cell reference is provided in the format `"AX"` (e.g., `"A1"`, `"B10"`), where the
    letter represents the column (from `'A'` to `'Z'`) and the number represents a
    **1-indexed** row.

    * `void resetCell(String cell)` Resets the specified cell to 0.

    * `int getValue(String formula)` Evaluates a formula of the form `"=X+Y"`, where `X`
    and `Y` are **either** cell references or non-negative integers, and returns the
    computed sum.

    **Note:** If `getValue` references a cell that has not been explicitly set using
    `setCell`, its value is considered 0.
    
    
    Your Spreadsheet object will be instantiated and called as such:
        obj = Spreadsheet(rows)
        obj.setCell(cell,value)
        obj.resetCell(cell)
        param_3 = obj.getValue(formula)
    """

    def __init__(self, rows: int):
        # Store the number of rows for potential validation (though not enforced here)
        self.rows = rows
        # Use a dictionary to store cell values sparsely, key as (column_letter, row_number)
        self.grid = {}

    def set_cell(self, cell: str, value: int) -> None:
        # Parse column letter and 1-based row number from cell string
        col = cell[0]
        row = int(cell[1:])
        # Set the value in the grid
        self.grid[(col, row)] = value

    setCell = set_cell

    def reset_cell(self, cell: str) -> None:
        # Parse column and row as in setCell
        col = cell[0]
        row = int(cell[1:])
        # Remove the cell from grid if present, effectively resetting to 0
        self.grid.pop((col, row), None)

    resetCell = reset_cell

    def get_value(self, formula: str) -> int:
        # Split the formula after '=' into two parts separated by '+'
        parts = formula[1:].split('+')
        # Initialize sum to 0
        total = 0
        # Process each part (X and Y)
        for part in parts:
            if part.isdigit():
                # If part is a digit string, convert to int and add
                total += int(part)
            else:
                # Otherwise, parse as cell reference
                col = part[0]
                row = int(part[1:])
                # Get value from grid or default to 0, add to total
                total += self.grid.get((col, row), 0)
        # Return the computed sum
        return total

    getValue = get_value