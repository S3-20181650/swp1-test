import random
class updown:
    def new(self, limit):
        self.b=random.randint(1,limit)
        self.count=0
    def answer(self):
        return self.b
    def start(self,guess_number):
        if  guess_number> self.b:
                self.count+=1
                return "DOWN"
        if  guess_number< self.b:
                self.count+=1
                return "UP"
        if guess_number== self.b:
                self.count+=1
                return "Success! 정답을 맞추는데 총 {}회 걸렸습니다.".format(self.count)
if __name__=="__main__":
    s=updown()
    guess_number=0
    limit=int(input())
    s.new(limit)
    while s.answer()!=guess_number:
        guess_number=int(input())
        if limit < guess_number:
            print("Error! 다시 입력하세요")
        else:
            print(s.start(guess_number))
