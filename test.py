from typing import List

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.stack = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        while len(self.stack) - 1 != self.index:
            self.stack.pop()
        self.stack.append(url)
        self.index += 1
        

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
        return self.stack[self.index]
        

    def forward(self, steps: int) -> str:
        self.index += steps
        stack_size = len(self.stack)
        if stack_size <= self.index:
            self.index = stack_size - 1
        return self.stack[self.index]



# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("homepage")
obj.visit("url")
obj.visit("url")

param_2 = obj.back(1)
print(param_2)
param_3 = obj.forward(1)
print(param_3)
