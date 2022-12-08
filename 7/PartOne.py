#
# From https://topaz.github.io/paste/#XQAAAQAuCgAAAAAAAAAxmwhIY/U96SugLXgINfPgWYrE3Nau8NOhgIbrf5usfSUThAnfL83FCakFds7byRWcM6MMNHSN1/nR8PMsolbiy71BE9P4q8ladzEzMwVh2VecQSZKiV8gKPYhKU3rqehurhTLUwUEII0QW3l6Isk+EkBIQrHxhJCZYN7vV0bqN1nydsn1P+q2aJdpPA2/FXResYjKY9QZjwA/GCpb3/dWojpqpvQeTd/Z9Y7f8L1NLO8oJO85xbSGNviT1RxCvAEESWMgeXgvsG63pyuP+isifEESl0O3TLdPgk+vevmTm1NY/nYK0CfAnrqb45N5q4IezVWBddwCkPA5L7ej0yIFe2Js9jaJ3seolESuFapy3/6DY1qtc48OSvqAPZHtUWHexJGGbFZhIjAF4KcxG0WA4NCikYFaH+Om59Btr4mbbHgArAYvEErIc4N8fVH1Y4PL1DlLzSh7s1lVdFgWZkMRvPBI5ItC8ma2hMwQljCwng78W7KeZrDyFzYOJWEYmgDKIfhOJAOTTsxMwTzBLSKbJTpdYUU+bcC1qDH2sWIWJboI93kZTsaj04GfpNFHE6sU8U32sNlaM3fr+waABnwZ9VjIbG9YExGgi1SEhHbJ36yTugj/aNKAdYRrQAkKsel7z0cEQLlRixsFMhGz5UurwxMgYhYR5eoLmlqXDr1CbpjVCRx4N46CLuUcxRm2b4l2qJMgL7+48oq6dlDx7gvZMT0STmkz1I0bbIJvd1Rrd85ftRjCEBftKw12SOcmLQ/25yTF05GhF684OykEiiQeBRyr0x//XiJVKLA9aoReyJTzkIsQSLF89dbomHXmvOiUFBQmt39qsp3dQGvCSIxwaR55Mo57bIsvrMLvNXoG0Lh/w7d0YDzUJoGW2zipFvAnZlKSc+iS0fuqgihCRNJ7WahZdjuRqKEdI6YKlFqq2KUQ0bMvi4Ku/IcBQH9nrOp+aLqduUbwRIwARzT4gQ6NL3kXB6afoocmHCdfGktS588e8C5yaY+uFl9n8gpX3Qr3axvtky8wCTZlyEg/PF1I0DtIVEvll0TEZoOxcFs+uUXoguIlzWOXXDn+JkHXxq737HY0peQ+op79Q3SrzsSX8RwV5q5b880nOzbLbWfb64DGs0VJGG4+YrQAUuL/tW6hhA==
#

class File:
    def __init__(self, name: str, fileSize: int):
        self.name = name
        self.size = fileSize

    def __str__(self) -> str:
        return f"{self.name} - {self.size}"


class Directory:
    subdiretories: []
    files: [File]

    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.subdiretories = []
        self.files = []

    def size(self) -> int:
        total = 0
        for sub in self.subdiretories:
            total += sub.size()

        for file in self.files:
            total += file.size

        return total

    def addSub(self, other):
        self.subdiretories.append(other)

    def addFile(self, file: File):
        self.files.append(file)

    def __str__(self) -> str:
        rv = f"Dir: {self.name} - {self.size()}\n"
        for file in self.files:
            rv += f"\t File: {file}\n"

        for sub in self.subdiretories:
            rv += f"\t {sub}\n"

        return rv


def checkAllowedDirs(currDir: Directory):
    for sub in currDir.subdiretories:
        if sub.size() < 100000:
            allowedDirs.append(sub)

        checkAllowedDirs(sub)


def checkDeletable(currDir: Directory):
    for sub in currDir.subdiretories:
        if sub.size() >= SPACENEEDEDTOBECLREAED:
            possibleDeletes.append(sub)
        checkDeletable(sub)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        raw = [line.replace("\n", "") for line in f.readlines()]

    currentlyLS = False

    fileSystem = Directory("ROOT", "")
    currentDir: Directory = fileSystem

    for line in raw:
        if line.startswith("$"):
            if "cd" in line:
                where = line.split(" ")[2]
                if where == "..":
                    currentDir = currentDir.parent
                else:
                    createdDir = Directory(where, currentDir)
                    currentDir.addSub(createdDir)
                    currentDir = createdDir
        else:
            size, currentName = line.split(" ")
            if size.isnumeric():
                currentDir.addFile(File(currentName, int(size)))

    allowedDirs = []
    checkAllowedDirs(fileSystem)
    print(f"Solution 1: {sum([allowedDir.size() for allowedDir in allowedDirs])}")

    possibleDeletes = []

    TOTALSPACE = 70000000
    SPACEREQUIRED = 30000000
    USEDSPACE = fileSystem.size()
    SPACENEEDEDTOBECLREAED = SPACEREQUIRED - (TOTALSPACE - USEDSPACE)

    checkDeletable(fileSystem)

    print(f"Solution 2: {min([possibleDelete.size() for possibleDelete in possibleDeletes])}")
