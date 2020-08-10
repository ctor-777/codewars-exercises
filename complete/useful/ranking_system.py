
#Write a class called User that is used to calculate the amount that a 
# user will progress through a ranking system similar to the one Codewars 
# uses.

#Business Rules:
#   -A user starts at rank -8 and can progress all the way to 8.
#   -There is no 0 (zero) rank. The next rank after -1 is 1.
#   -Users will complete activities. These activities also have ranks.
#   -Each time the user completes a ranked activity the users rank progress
#     is updated based off of the activity's rank
#   -The progress earned from the completed activity is relative to what
#     the user's current rank is compared to the rank of the activity
#   -A user's rank progress starts off at zero, each time the progress 
#     reaches 100 the user's rank is upgraded to the next level
#   -Any remaining progress earned while in the previous rank will be 
#     applied towards the next rank's progress (we don't throw any progress 
#     away). The exception is if there is no other rank left to progress 
#     towards (Once you reach rank 8 there is no more progression).
#   -A user cannot progress beyond rank 8.
#   -The only acceptable range of rank values is 
#     -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should 
#     raise an error.

#The progress is scored like so:
#   -Completing an activity that is ranked the same as that of the user's 
#     will be worth 3 points
#   -Completing an activity that is ranked one ranking lower than the 
#     user's will be worth 1 point
#   -Any activities completed that are ranking 2 levels or more lower 
#     than the user's ranking will be ignored
#   -Completing an activity ranked higher than the current user's rank 
#     will accelerate the rank progression. The greater the difference 
#     between rankings the more the progression will be increased. The 
#     formula is 10 * d * d where d equals the difference in ranking 
#     between the activity and the user.

#Logic Examples:
#   -If a user ranked -8 completes an activity ranked -7 
#     they will receive 10 progress.
#   -If a user ranked -8 completes an activity ranked -6 
#     they will receive 40 progress.
#   -If a user ranked -8 completes an activity ranked -5 
#     they will receive 90 progress.
#   -If a user ranked -8 completes an activity ranked -4 
#     they will receive 160 progress, resulting in the user being 
#     upgraded to rank -7 and having earned 60 progress towards their 
#     next rank.
#   -If a user ranked -1 completes an activity ranked 1 
#     they will receive 10 progress (remember, zero rank is ignored)

#----------------------------Problem solution----------------------------
minimun_rank = -8
maximun_rank = 8
valid_ranks = [i for i in range(minimun_rank, maximun_rank + 1)]
valid_ranks.remove(0)
class User_codewars:
    def __init__(self, rank = -8, progress = 0, valid_ranks = valid_ranks):
        if rank in valid_ranks:
            self.rank = rank
        self.progress = progress
        self._valid_ranks = valid_ranks

    def _check_rank(self):
        while self.progress >= 100:        
            rank_index = self._valid_ranks.index(self.rank)
                
            self.rank = self._valid_ranks[rank_index + 1]
            self.progress -= 100
    
        rank_index = self._valid_ranks.index(self.rank)
        if rank_index == len(self._valid_ranks) - 1:
            self.progress = 0

    def inc_progress(self, activity_rank):
        activity_rank_index = self._valid_ranks.index(activity_rank)
        user_rank_index = self._valid_ranks.index(self.rank)
        
        if activity_rank not in self._valid_ranks:
            raise ValueError("the activity rank isn't valid")
        
        if activity_rank_index == user_rank_index - 1:
            self.progress += 1
        elif activity_rank_index == user_rank_index:
            self.progress += 3
        elif activity_rank_index > user_rank_index:
            difference = activity_rank_index - user_rank_index
            self.progress += 10 * (difference ** 2)

        self._check_rank()
        
#----------------------------Useful solution----------------------------

class User:
    """this class creates a user in a ranking system.
    
        the ranking system follows the next rules:
            -the user have a rank,reachable by rank ptivate variable.
            -the activities also have a rank defined when the 
              inc_progress finction is called
            -the user have a progress, when the progress reaches 100 its 
              substractes 100 and added a rank to the user, when the user 
              reaches the maximun rank the progress will be ever 0.
            -activities 2 ranks or more under user rank will be ignored
            -activities 1 rank under user will give user 1 progress point
            -activities at the same rank as user will give user 3 
              progress points
            -activies 1 or more ranks over user will give progress 
              points according to this formula: 10 * (d ** 2), where 
              d is the difference between user rank and activity rank
              
        param:
            rank(depends on ranks types): defines the initial rank
                of the user. has to be in valid ranks
            progress(int): defines the initial progress of the user
            valid_ranks(list/tuple): here is where defines the ranks, 
              content can be any data type, the ranks are orderd in the 
              list/tuple order.
    """
    def __init__(self, rank, progress, valid_ranks):
        #verifing the data types of inputs
        if rank not in valid_ranks:
            raise ValueError("specified rank is not in valid ranks")

        if type(progress) != int:
            raise TypeError(f"the initial progress have to be a integer, and you introduced an {type(progress)}")

        if type(valid_ranks) not in [tuple, list]:
            raise TypeError(f"the valid_keys variable heve to be a list or a tuple, you introduced a {type(valid_ranks)}")
        
        #asigning local variables
        self.rank = rank
        self.progress = progress
        self._valid_ranks = valid_ranks

    def _check_rank(self):
        #a private function to adjust the rank using progress points
        while self.progress >= 100:        
            rank_index = self._valid_ranks.index(self.rank)
                
            self.rank = self._valid_ranks[rank_index + 1]
            self.progress -= 100
    
        rank_index = self._valid_ranks.index(self.rank)
        if rank_index == len(self._valid_ranks) - 1:
            self.progress = 0

    def inc_progress(self, activity_rank):
        """add an activity and recalculate the rank and progression of user.
            
            param:
                activity_rank: the rank of the activity, have to be in valid_ranks.
        """
        
        activity_rank_index = self._valid_ranks.index(activity_rank)
        user_rank_index = self._valid_ranks.index(self.rank)
        
        if activity_rank not in self._valid_ranks:
            raise ValueError("the activity rank isn't valid")
        
        if activity_rank_index == user_rank_index - 1:
            self.progress += 1
        elif activity_rank_index == user_rank_index:
            self.progress += 3
        elif activity_rank_index > user_rank_index:
            difference = activity_rank_index - user_rank_index
            self.progress += 10 * (difference ** 2)

        self._check_rank()
