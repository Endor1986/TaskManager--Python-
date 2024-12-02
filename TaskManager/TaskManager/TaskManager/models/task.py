class Task:
    def __init__(self, name: str, user: str, due_date, priority="medium"):
        self.name = name
        self.user = user
        self.due_date = due_date
        self.priority = priority
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{self.name} (User: {self.user}, Due: {self.due_date}, Priority: {self.priority}) {status}"
