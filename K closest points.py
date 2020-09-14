import random
class Solution:

    def distance(self,given_array):
        return given_array[0]**2+given_array[1]**2

    def distance_list(self,points_array):
        new=[]
        for i in range(len(points_array)):
            dist=self.distance(points_array[i])
            new.append([points_array[i],dist])
        
        return new
    
    def find_minimum(self,distance_array,k):

        if k==len(distance_array):
            final_array=[]
            for i in range(len(distance_array)):
                final_array.append(distance_array[i][0])
            
            return final_array
        
        random_point=random.choice(distance_array)
        pivot_point=random_point[1]
        left = []
        pivot=[]
        right=[]
        i=0
        while i < len(distance_array):
            current=distance_array[i]
            current_distance=current[1]
            if current_distance<pivot_point:
                left.append(current)
            if current_distance==pivot_point:
                pivot.append(current)
            if current_distance>pivot_point:
                right.append(current)

            i+=1

        len_left=len(left)
        
        if k==len_left:
            final_array=[]
            for i in range(len(left)):
                final_array.append(left[i][0])
            
            return final_array
            
        
        if k==len_left+len(pivot):
            return [i[0] for i in left]+[i[0] for i in pivot]
        
        if k<len_left:
            return self.find_minimum(left,k)
        
        else:
            return [i[0] for i in left]+[i[0] for i in pivot]+self.find_minimum(right,k-len(left)-len(pivot))
            
            
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        x=self.distance_list(points)
        return self.find_minimum(x,K)