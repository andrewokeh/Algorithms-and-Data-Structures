# Note: Can be done more efficiently with array, this solution is for doubly linked list practice

class ListNode:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        

    def visit(self, url: str) -> None:
        new_page = ListNode(url)

        self.curr.next = new_page
        new_page.prev = self.curr
        
        self.tail.prev = new_page
        new_page.next = self.tail
        
        self.curr = new_page
        

    def back(self, steps: int) -> str:
        while self.curr and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        
        if steps == 0 and self.curr:
            return self.curr.val
        else:
            self.curr = self.head
            return self.head.val
        

    def forward(self, steps: int) -> str:
        while self.curr and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        
        if steps == 0 and self.curr and self.curr != self.tail:
            return self.curr.val
        else:
            self.curr = self.tail.prev
            return self.tail.prev.val
                


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
