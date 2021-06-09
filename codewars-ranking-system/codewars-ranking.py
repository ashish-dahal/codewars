RANK = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)

class User:
    def __init__(self):
        self.rank = RANK[0]
        self.progress = 0
        self.rank_index = 0
        
    def inc_progress(self, activity_rank):
        # Check is activity rank is valid
        if activity_rank not in RANK:
            raise Exception('Sorry! The activity rank is invalid.')
        activity_rank_index = RANK.index(activity_rank)
        
        # Calculate the progress
        if activity_rank_index == self.rank_index:
            self.progress += 3
        elif activity_rank_index == self.rank_index - 1:
            self.progress += 1
        elif activity_rank_index > self.rank_index:
            self.progress += 10*(activity_rank_index - self.rank_index)**2
            
        # Assign the rank based on progress progress
        if self.progress >= 100 and self.rank_index < 15:
                self.rank_index += self.progress//100
                self.rank = RANK[self.rank_index] if self.rank_index <= 15 else 8
                self.progress %= 100
        if self.rank == 8:
            self.progress = 0
