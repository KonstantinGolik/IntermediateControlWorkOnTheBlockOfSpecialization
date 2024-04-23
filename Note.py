class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

    def __repr__(self):
        return f"ID: {self.id} Дата/время: {self.timestamp}\nЗаголовок: {self.title}\n{self.body}\n"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }