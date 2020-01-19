class Link:
    """A linked list"""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def f():
    return (1, 2, 3)

def main():
    xyz_vals = Link.empty
    for _ in range(3):
        xyz_vals = Link(f(), xyz_vals)
    print(xyz_vals)

    file_name = "test.txt"
    file = open(file_name, 'w')
    while xyz_vals is not Link.empty:
        xyz = ", ".join([str(x) for x in xyz_vals.first])
        file.write(xyz + '\n')
        xyz_vals = xyz_vals.rest
    file.close()
    
if __name__ == "__main__":
    main()