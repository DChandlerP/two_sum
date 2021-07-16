import two_sum

class Test_Two_sum_Two_sum:
    def test_two_sum_1(self):
        result = two_sum.two_sum([0, 1, 2, 8, 22], 10)
        assert result == [2, 8]
