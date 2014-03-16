class Romans:

    def __init__(self, value):
        if type(value) == str:
            self._str = value
            self._num = Romans.str_to_num(value)
        elif type(value) == int:
            self._str = ""
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
