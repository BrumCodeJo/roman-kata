class Romans:

    def __init__(self, value):
        if type(value) == str:
            self._str = value
            self._num = Romans.str_to_num(value)
        elif type(value) == int:
            self._str = Romans.num_to_str(value)
            self._num = value

    def __str__(self):
        return self._str

    def __int__(self):
        return self._num

    @staticmethod
    def str_to_num(value):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = [values.get(i) for i in value]

        for i in range(len(result)):
            if result[i] < result[min(len(result)-1, i+1)]:
                result[i] *= -1

        return sum(result)

    @staticmethod
    def num_to_str(value):
        values = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        result = ""
        for v in sorted(values.keys(), reverse=True):
            unit_count = value // v
            result += values[v] * unit_count
            value -= unit_count * v

        result = result.replace("VIIII", "IX").replace("LXXXX", "XC").replace("DCCCC", "CM")
        return result.replace("IIII", "IV").replace("XXXX", "XL").replace("CCCC", "CD")
