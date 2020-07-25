class Solution:
    def reverse(self, x: int) -> int:
       
        new=str(x)
  
        if x<0:
            new[0]=="-"
            new=new.replace("-",'')
            new="-"+new[::-1]
            a=int(new)
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
            return int(new)
        if x>0:
            a=int(new[::-1])
            if a >= -2147483648 and a<= 2147483647:
               return a
            else:
               return 0
            return int(new[::-1])
        if x==0:
            return x
