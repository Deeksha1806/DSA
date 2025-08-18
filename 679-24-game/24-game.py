class Solution:
    def upgrade(self, way: int):
        match way:
            case 1:
                return

            case 2:
                self.expression = '(' + self.expression[:3] + ')' + self.expression[3:]

            case 3:
                self.expression = '(' + self.expression[:5] + ')' + self.expression[5:]

            case 4:
                self.expression = self.expression[:2] + '(' + self.expression[2:5] + ')' + self.expression[5:]

            case 5:
                self.expression = self.expression[:4] + '(' + self.expression[4:] + ')'

            case 6:
                self.expression = self.expression[:2] + '(' + self.expression[2:] + ')'

            case 7:
                self.expression = '(' + self.expression[:3] + ')' + self.expression[3] + '(' + self.expression[4:] + ')'

            case 8:
                self.expression = '((' + self.expression[:3] + ')' + self.expression[3:5] + ')' + self.expression[5:]

            case 9:
                self.expression = '(' + self.expression[:2] + '(' + self.expression[2:5] + '))' + self.expression[5:]

            case 10:
                self.expression = self.expression[:2] + '((' + self.expression[2:5] + ')' + self.expression[5:] + ')'

            case 11:
                self.expression = self.expression[:2] + '(' + self.expression[2:4] + '(' + self.expression[4:] + '))'



    def judgePoint24(self, cards: List[int]) -> bool:
        operations = ('+', '-', '*', '/')
        opers = list(product(operations, repeat=3))

        for k in range(1, 12):
            for crds in permutations(cards):
                for j in opers:
                    self.expression: str = ""

                    for i in range(3):
                        self.expression += str(crds[i])
                        self.expression += j[i]

                    self.expression += str(crds[-1])
                    self.upgrade(k)

                    try:
                        if abs(24 - eval(self.expression)) <= 0.00000001:
                            return True

                    except ZeroDivisionError:
                        pass

        return False