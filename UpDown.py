import random
class updown:
    def new(self, limit):
        self.b=random.randint(1,limit)
        self.count=0
	self.l=limit
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
	if guess_number <0 :
		response= "Error! put only natural number"
	if guess_number > self.l:
		response= "Error! guess number can't bigger than limit"
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
            print(s.start(guess_number))
        if s.b==guess_number:
            print(s.start(guess_number),"in {}.".format(s.total()))
        else:
            print(s.start(guess_number))
