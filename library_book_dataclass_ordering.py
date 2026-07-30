from dataclasses import dataclass, field

@dataclass(order=True)
class LibraryBook:
    sort_index: list = field(init=False, repr=False)
    title: str
    author: str
    pages: int
    tags: list = field(default_factory=list)

    def __post_init__(self):
        self.sort_index = [self.title, self.author, self.pages]

LibraryBook1 = LibraryBook("Rich dad and Poor dad", "Keyoski", 500)
LibraryBook2 = LibraryBook("The Alchemist", "Paulo Coelho", 200)

print(LibraryBook1 < LibraryBook2)
print(LibraryBook1.sort_index)
print(LibraryBook2.sort_index)
