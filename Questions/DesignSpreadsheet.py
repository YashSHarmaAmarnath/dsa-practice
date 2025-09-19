class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        x,y = get_cell_cord(cell)
        self.sheet[x][y] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell,0)

    def getValue(self, formula: str) -> int:
        def checker(cell):
            if cell[0].isdigit():
                return False
            else:
                return True
        val = formula.split('+')
        if checker(val[0][1:]):
            x,y = get_cell_cord(val[0][1:])
            n1 = self.sheet[x][y]
        else:
            n1 = int(val[0][1:])
        if checker(val[1]):
            x,y = get_cell_cord(val[1])
            n2 = self.sheet[x][y]
        else:
            n2 = int(val[1])
        return n1+n2
def get_cell_cord(cell):
    col = get_col_num(cell[0])  
    row = int(cell[1:]) - 1     
    return (row, col)
def get_col_num(x):
    return ord(x) - ord('A') 


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
