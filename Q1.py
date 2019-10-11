num=int(input("Enter Case:"))
for i in range(1,num+1):
    nflr=int(input("now enter 1<=No of floor<=1000"))
    ppos=int(input("now enter 1<=Person Pos.<=1000"))
    dpos=int(input("now enter 1<=Dest. Pos.<=1000"))
    lpos=int(input("now enter 1<=Lift Pos.<=1000"))
    ptime=int(input("now enter 1<=Person Time<=60"))
    ltime=int(input("now enter 1<=Lift Time<=60"))
    tsec=0
    if(1<=nflr,ppos,lpos,dpos<=1000 and 1<=ltime,ptime<=60 and nflr>=ppos,lpos,dpos):
        if(ppos==dpos):
            print("nothing to go")
            pass
        elif(ppos==lpos):
            if(ltime>ptime):
                print("STAIRS")
                pass
            else:
                print("ELEV")
                pass
        elif(ppos<dpos):  
            pgap=dpos-ppos 
            psec=ptime*pgap
            if(lpos>ppos):
                lgap=lpos-ppos
                lsec=lgap*ltime
                if(lsec>psec):
                    print("STAIRS")
                    pass
                else:
                    tsec=ltime*(lgap+pgap)
                    if(tsec>psec):
                        print("STAIRS")
                        pass
                    else:
                        print("ELEV")
                        pass
            elif(ppos>lpos): 
                lgap=ppos-lpos
                lsec=lgap*ltime
                if(lsec>psec):
                    print("STAIRS")
                    pass
                else:
                    tsec=ltime*(lgap+pgap)
                    if(tsec>psec):
                        print("STAIRS")
                        pass
                    else:
                        print("ELEV")
                        pass
        elif(dpos<ppos):
            pgap=ppos-dpos
            psec=ptime*pgap
            if(ppos<lpos):
                lgap=lpos-ppos
                lsec=lgap*ltime
                if(psec<lsec):
                    print("STAIRS")
                    pass
                else:
                    tsec=ltime*(lgap+pgap)
                    if(tsec>psec):
                        print("STAIRS")
                        pass
                    else:
                        print("ELEV")
                        pass
            elif(lpos<ppos):
                lgap=ppos-lpos
                lsec=lgap*ltime
                if(lsec>psec):
                    print("STAIRS")
                    pass
                else:
                    tsec=ltime*(lgap+pgap)
                if(tsec>psec):
                    print("STAIRS")
                    pass                    
                else:        
                    print("ELEV")
                    pass
    else:
        print("you enter wrong values")
        pass
