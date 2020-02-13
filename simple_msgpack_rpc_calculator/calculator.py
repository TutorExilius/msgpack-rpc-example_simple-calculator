class Calculator(object):
    def sum(self, x, y):
        result = x + y
        print(f"Response to: sum({x}, {y}) with result: {result}", flush=True)
        return result

    def sub(self, x, y):
        result = x - y
        print(f"Response to: sub({x}, {y}) with result: {result}", flush=True)
        return result

    def mul(self, x, y):
        result = x * y
        print(f"Response to: mul({x}, {y}) with result: {result}", flush=True)
        return result

    def div(self, x, y):
        result = x / y
        print(f"Response to: div({x}, {y}) with result: {result}", flush=True)
        return result
