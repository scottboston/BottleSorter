class Bottle:
    """Bottle Class"""

    def __init__(self, volume, name):
        self.volume = volume
        self.contents = []
        self.name = name

    def draw_bottle(self) -> None:
        """To be used later"""
        print("+-----+")
        for i in range(self.volume, -1, -1):
            # print('|     |')
            if i < len(self.contents):
                print(f"|  {self.contents[i]}  |")
            else:
                print(f"|     |")
            # print('|     |')
        print("+-----+")

    def add_contents(self, letter) -> None:
        """Add content to bottle with checks for volume"""
        if len(self.contents) < self.volume:
            self.contents.append(letter)
        else:
            print("Bottle is full")

    def remove_contents(self) -> str:
        """Remove the top level from a bottle"""
        return self.contents.pop()

    def show_contents(self) -> tuple[str, list]:
        """Show contents of bottle with label"""
        return self.name, self.contents

    def has_room(self) -> bool:
        """Is the bottle full?"""
        return len(self.contents) < self.volume

    def valid_pour(self, content) -> bool:
        """Is it a valid pour either empty or contents pour matches the top layer in the bottle"""
        return (
            len(self.contents) == 0 or self.has_room() and self.contents[-1] == content
        )

    def is_bottle_complete(self):
        """Is the bottle full, with one color only or empty"""
        result = (
            len(self.contents) == self.volume and len(set(self.contents)) == 1
        ) or (len(self.contents) == 0)
        return result
