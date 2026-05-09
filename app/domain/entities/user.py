class User:
    def __init__(
        self,
        id=None,
        username="",
        password="",
        role="employee"
    ):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
