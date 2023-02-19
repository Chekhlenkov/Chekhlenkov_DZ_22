class Unit:

    # ...
    def __init__(self):
        pass

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'up':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'down':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'left':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'right':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
