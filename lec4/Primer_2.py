def countbeatingrooks(rookcoords):
    def addrook(rowocol, key):
        if key not in rowocol:
           rowocol[key] = 0
        rowocol[key] += 1

    def countpars(rowocol):
        pairs = 0
        for key in rowocol:
            pairs += rowocol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)

    return countpars(rooksinrow) + countpars(rooksincol)
