from collections import deque
class Lift:
    def __init__(self, nflr,lpos):
        self.nflr=nflr
        self.lps=lpos
        self.strt=deque()
        self.endp=deque()
        self.lft=dict()
    def acceptppl(self):
        a=''
        b=''
        self.pplc=int(input("No. of People request <={0}:".format(self.nflr)))
        print("Input Person From,TO value of Floors <={0}:".format(self.nflr))
        for i in range(0,self.pplc):
            a=input("where You are?")
            b=input("where You want to go?")
            self.lft[a]=b
    def runlift(self):
        if(bool(self.lft)):
            while(bool(self.lft)):
                i=int(list(self.lft.keys())[0])
                self.strt.append(i)
                self.endp.append(int(self.lft.get(str(i))))
                print("Lift is going to:{0}".format(i))
                print("Adding:{0} for {1}".format(i,int(self.lft.get(str(i)))))
                del self.lft[str(i)]
                while(self.endp):
                    if(i>int(self.endp[0])):
                        i=i-1
                        print("Lift is going to:{0}".format(i))
                        if(bool(self.lft.get(str(i)))):
                            self.strt.append(i)
                            self.endp.append(int(self.lft.get(str(i))))                           
                            print("Adding:{0} for {1}".format(i,int(self.lft.get(str(i)))))
                            del self.lft[str(i)]                        
                        if(bool(self.endp.count(i))):                            
                            print("Removing:{0} of {1}".format(i,self.strt[self.endp.index(i)]))
                            del self.strt[self.endp.index(i)]
                            self.endp.remove(i)                           
                        pass
                    elif(i<int(self.endp[0])):
                        i=i+1
                        print("Lift is going to:{0}".format(i))
                        if(bool(self.lft.get(str(i)))):
                            self.strt.append(i)
                            self.endp.append(int(self.lft.get(str(i))))
                            print("Adding:{0} for {1}".format(i,int(self.lft.get(str(i)))))
                            del self.lft[str(i)]
                        if(bool(self.endp.count(i))):
                            print("Removing:{0} of {1}".format(i,self.strt[self.endp.index(i)]))
                            del self.strt[self.endp.index(i)]
                            self.endp.remove(i)
                        pass
                    elif(self.endp.count(i)):                        
                        if(bool(self.lft.get(str(i)))):
                            self.strt.append(i)
                            self.endp.append(int(self.lft.get(str(i))))
                            print("Adding:{0} for {1}".format(i,int(self.lft.get(str(i)))))
                            del self.lft[str(i)]
                        if(bool(self.endp.count(i))):
                            print("Removing:{0} of {1}".format(i,self.strt[self.endp.index(i)]))
                            del self.strt[self.endp.index(i)]
                            self.endp.remove(i)
                        pass

            print("Now Lift is empty..")
        else:
            print("No work")
            pass

nflr=int(input("No of Floor:"))
lpos=int(input("Lift Pos<{0}:".format(nflr)))
if(lpos>nflr):
    print("wrong value")
    pass
else:
    l=Lift(nflr,lpos)
    l.acceptppl()
    l.runlift()