from Novoice_Pytest.Revision.oopsDemo import Calculator


class Childimpl(Calculator):
    num2 = 200

    def getcompleteData(self):
        return self.num2 + self.num + self.sumation()

obj = Childimpl(2,3)
print(obj.getcompleteData())