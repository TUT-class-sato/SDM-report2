


test_string=["1","999","0","1000","0.999","999.001","\"a\""]

num=1
for st1 in test_string:
    for st2 in test_string:
        ans=-1
        if st1.isdecimal() and st2.isdecimal():
            if int(st1)>0 and int(st1)<1000 and int(st2)>0 and int(st2)<1000:
                ans=int(st1)*int(st2)
        string="""
    def test_case%d (self):
        self.assertEqual (%s, calc(%s,%s))"""%(num,str(ans),st1,st2)
        print(string)
        num+=1
