# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring



class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони має бути більше 0.")
        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має бути в межах від 0 до 180 градусів.")


        super().__setattr__(key, value)
        if key == "angle_a":
            super().__setattr__("angle_b", 180 - value)

    def __repr__(self):
        return f"Romb (side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"



rhombus = Romb(17, 80)
print(rhombus)
