class FactorsOfNumbers():
    def getPrimeFactor(self):
        print(f"All prime factors of {self.num} are:")
        num = self.num
        for i in range(2, num + 1):
            isPrime = True
            if num % i == 0:
                for j in range(2, i // 2 + 1):
                    if j % 2 == 0:
                        isPrime = False
                        break
                if isPrime == True:
                    print(i)


primeFactor = FactorsOfNumbers()
primeFactor.num = 12
primeFactor.getPrimeFactor()