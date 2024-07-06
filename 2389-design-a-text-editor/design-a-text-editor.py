class TextEditor:

    def __init__(self):
        self.s = ""
        self.cur = 0

    def addText(self, text: str) -> None:
        if self.cur >= len(self.s):
            self.s=self.s+text
            self.cur += len(text)
        else:
            self.s = self.s[:self.cur]+text+self.s[self.cur:]
            self.cur += len(text)

    def deleteText(self, k: int) -> int:
        if self.cur == 0:
            return 0
        
        # Calculate the number of characters to delete
        delete_count = min(k, self.cur)
        
        # Delete the text
        self.s = self.s[:self.cur - delete_count] + self.s[self.cur:]
        self.cur -= delete_count
        return delete_count

    def cursorLeft(self, k: int) -> str:
        self.cur = max(0, self.cur - k)
        start = max(0, self.cur - 10)
        return self.s[start:self.cur]

    def cursorRight(self, k: int) -> str:
        self.cur = min(len(self.s), self.cur + k)
        start = max(0, self.cur - 10)
        return self.s[start:self.cur]
