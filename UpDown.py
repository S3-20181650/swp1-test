import random
class updown:
    def new(self, limit):
        self.b=random.randint(1,limit)
        self.count=0
    def start(self,guess_number):
        if  guess_number> self.b:
                self.count+=1
                response = "DOWN"
        if  guess_number< self.b:
                self.count+=1
                response= "UP"
        if guess_number== self.b:
                self.count+=1
                response= "Success!"
        return response
    def total(self):
        return self.count
if __name__=="__main__":
    s=updown()
    guess_number=0
    limit=int(input())
    s.new(limit)
    while s.b!=guess_number:
        guess_number=int(input())
        if limit < guess_number:
            print("Error! 다시 입력하세요")
        if s.b==guess_number:
            print(s.start(guess_number),"맞추는데 걸린 횟수는 {}입니다.".format(s.total()))
        else:
            print(s.start(guess_number))