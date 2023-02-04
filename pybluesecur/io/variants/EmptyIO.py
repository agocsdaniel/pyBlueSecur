class EmptyIO:
    def read(self):
        print("Used EmptyIO.read, this might be bad :(")
        pass

    def write(self, data):
        print("Used EmptyIO.write, this might be bad :(")
        pass