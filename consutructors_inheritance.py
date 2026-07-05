class biotech:
    def __init__(self):

        print("biotech is the stream")

class biochemistry(biotech):
    def __init__(self):
        super().__init__()
        print("biochemistry is a part of biotech")

biochem = biochemistry()

