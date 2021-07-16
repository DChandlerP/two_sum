import two_sum

class Test_Two_sum_TwoSum:
    def test_twoSum_1(self):
        result = two_sum.twoSum([0, 2, 8, 11], 10)
        assert result == [1, 2]
