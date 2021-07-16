import two_sum

class Test_Two_sum_TwoSum:
    def test_twoSum_1(self):
        result = two_sum.twoSum([0, 1, 2, 8, 22], 10)
        assert result == [2, 3]

    def test_twoSum_2(self):
        result = two_sum.twoSum([0, 0], 3)
        assert result == []
