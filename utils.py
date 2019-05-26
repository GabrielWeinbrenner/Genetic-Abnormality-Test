import math
import cv2


RED = (0, 0, 255)

GREEN = (0, 255, 0)

BLUE = (255, 0, 0)


def is_pressed(key):

    return cv2.waitKey(1) & 0xFF == ord(key)


class Vector2:
    """2D vector implementation: Vector3(x, y)"""

    def __init__(self, x=0.0, y=0.0):
        """Vector2.__init__(x, y) -> None
        takes two arguments: x, y"""

        self.x = x

        self.y = y

    @property
    def magnitude(self):

        return (self.x ** 2 + self.y ** 2)**(1/2)

    def get_magnitude(self):

        return self.magnitude

    @property
    def angle(self):

        return self.get_angle()

    @property
    def unit(self):

        try:

            return self / self.magnitude

        except ZeroDivisionError:

            return self

    def __add__(self, other):

        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):

        return self * -1

    def to_int(self):

        return Vector2(int(self.x), int(self.y))

    def __sub__(self, other):

        return Vector2(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):

        return Vector2(self.x / other, self.y / other)

    def __mul__(self, other):

        if isinstance(other, Vector2):

            return self.dot(other)

        else:

            return Vector2(other * self.x, other * self.y)

    def __iadd__(self, other):

        return self + other

    def __isub__(self, other):

        return self - other

    def __imul__(self, other):

        return self * other

    def dot(self, other):

        return self.x * other.x + self.y * other.y

    def __str__(self):

        return f'<{self.x}, {self.y}>'

    @property
    def tuple(self):

        return self.x, self.y

    def __eq__(self, other):

        return other.tuple == self.tuple

    def __gt__(self, other):

        return self.magnitude > other.magnitude

    def __lt__(self, other):

        return self.magnitude < other.magnitude

    def angle_between(self, other):

        return math.atan2(other.y - self.y, other.x - self.x)

    def get_angle(self):

        return math.atan2(self.y, self.x)

    @staticmethod
    def from_angle(angle, magnitude=1.0):

        return Vector2(math.cos(angle)*magnitude, math.sin(angle)*magnitude)

    @staticmethod
    def zero():

        return Vector2(0, 0)

    def copy(self):

        return Vector2(self.x, self.y)

    @staticmethod
    def from_iterable(iterable):

        assert len(iterable) == 2

        return Vector2(*iterable)

    def distance(self, other):

        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Rectangle:

    def __init__(self, size, position=Vector2.zero()):

        self.size = size

        self.position = position

    def __str__(self):

        return f'|{self.size}, {self.position}|'

    def __repr__(self):

        return str(self)

    def get_position(self):

        return self.position

    def get_size(self):

        return self.size

    def set_position(self, position):

        self.position = position

    def set_size(self, size):

        self.size = size

    def inflate(self, factor):

        size = self.size * factor

        center = self.position + self.size / 2

        self.size = size

        self.position = center - size / 2

    def deflate(self, factor):

        self.inflate(1 / factor)

    def draw(self, image, border_color, border_width=1):

        cv2.rectangle(image, self.position.to_int().tuple, (self.position + self.size).to_int().tuple, border_color,
                      border_width)

    @staticmethod
    def from_iterable(iterable):

        assert len(iterable) == 4

        return Rectangle(Vector2(iterable[2], iterable[3]), Vector2(iterable[0], iterable[1]))

    @property
    def left(self):

        return self.position.copy()

    @property
    def top(self):

        return self.position.copy()

    @property
    def bottom(self):

        return Vector2(self.position.x, self.position.y + self.size.height)

    @property
    def right(self):

        return Vector2(self.position.x + self.size.x, self.position.y)

    @property
    def x(self):

        return self.position.x

    @property
    def y(self):

        return self.position.y

    @property
    def width(self):

        return self.position.x

    @property
    def height(self):

        return self.position.y
