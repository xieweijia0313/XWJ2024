from random import randint  # 生成随机数


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)
