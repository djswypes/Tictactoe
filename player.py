class Player:
    def __init__(self, avatar: str) -> None:
        self.__avatar = avatar
        self.score = 0
        self.positions = []

    def get_avatar(self):
      return self.__avatar