class Fizzbuzz:
    def call(self, number):
        if not self.is_int(number):
            raise ValueError()
        if number % 3 == 0:
            return "fizz"
        return ""

    def is_int(self, number):
        return isinstance(number, int)
