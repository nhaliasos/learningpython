
def solution(src,dest):
        global steps
        global globalsteps
        postlist=[]
        stepslist=[]
        steps=0
        bingo=dest
        bingoflag=False

        postlist=[src]
        
        def knight(postlist,bingo, bingoflag):
            global steps
            global globalsteps
            # global bingo
            # global bingoflag
            
            
            if steps==0:
                start=0
                end=1
            elif steps==1:
                start=1
                end=9
            else:
                start=8**(steps-1)+1
                end=start+8**steps
            
            for i in range(start,end):
                ipos=int(postlist[i])
                if ipos==bingo:
                    bingoflag=True
                    globalsteps=steps
                    break
                #if ipos<0:
                #    continue
                ipos_col=ipos % 8
                ipos_row=ipos // 8
                
                if ipos_row not in (0,1):
                    if ipos_col is not 0:
                        NL=ipos-17
                    else:
                        NL=-99
                    if ipos_col is not 7:
                        NR=ipos-15
                    else:
                        NR=-99
                else:
                    NL=-99
                    NR=-99
                postlist.append(NL)     
                postlist.append(NR)     
                
                if ipos_col not in (6,7):
                    if ipos_row is not 0:
                        EU=ipos-6
                    else:
                        EU=-99
                    if ipos_row is not 7:
                        ED=ipos+10
                    else:
                        ED=-99
                else:
                    EU=-99
                    ED=-99
                postlist.append(EU)
                postlist.append(ED)

                if ipos_row not in (6,7):
                    if ipos_col is not 7:
                        SR=ipos+17
                    else:
                        SR=-99
                    if ipos_col is not 0:
                        SL=ipos+15
                    else:
                        SL=-99
                else:
                    SR=-99
                    SL=-99
                postlist.append(SR)
                postlist.append(SL)

                if ipos_col not in (0,1):
                    if ipos_row is not 0:
                        WU=ipos-10
                    else:
                        WU=-99
                    if ipos_row is not 7:
                        WD=ipos+6
                    else:
                        WD=-99
                else:
                    WU=-99
                    WD=-99
                postlist.append(WU)    
                postlist.append(WD)
            
            steps=steps+1
            if not bingoflag:
                knight(postlist,bingo, bingoflag)
            return steps
        
        knight(postlist,bingo,bingoflag)
    
        return globalsteps

print('hello')
sol=solution(63,0)
print('the steps needed are..  %d' % sol)