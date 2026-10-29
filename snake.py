from random import randint


class Snake:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.body = []
        self.apple = [0,0]
        self.count = 0

    def update(self, dtx: int, dty: int, empty_cells) -> None:
        if [self.x, self.y] == self.apple:
            self.body.append((self.x, self.y))
            rnd_num = randint(0, len(empty_cells) - 1)
            self.apple = empty_cells[rnd_num]
            self.count += 1
        elif self.body:
            self.body.pop(0)
            self.body.append([self.x, self.y])

        self.x += dtx
        self.y += dty