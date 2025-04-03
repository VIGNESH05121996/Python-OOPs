import random

class FlipCoins():
    def toss(self):
        print(f"Number of times to flip the coin in {self.times}")
        t = 0
        h = 0
        for i in range(0, self.times):
            ran = random.uniform(0,1)
            if ran < 0.5:
                t = t + 1
            else:
                h = h + 1

        tails = (t / self.times) * 100
        heads = (h / self.times) * 100
        print(f"Percentage of heads is: {heads}")
        print(f"Percentage of tails is: {tails}")

flip = FlipCoins()
flip.times = 10
flip.toss()