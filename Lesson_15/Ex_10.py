'''Create a Python class representing a car with methods for accelerating and braking.'''


class Car:
    def __init__(self):
        self.speed = 0

    def accelerating(self, num):
        self.speed += num

    def braking(self, num):
        if self.speed >= num:
            self.speed -= num
        else:
            print('Invalid speed value')

    def check_speed(self):
        return self.speed
