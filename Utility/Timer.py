from time import time

class Timer:
    def start(self, run_time):
        self.start_time = time()
        self.end_time = time() + run_time
        self.run_time = run_time
    
    def is_done(self):
        current_time = time()
        return self.run_time < current_time - self.start_time
 
    def percent_done(self):
        current_time = time()
        return min(1, (current_time - self.start_time) / (self.end_time - self.start_time))

    def time_left(self):
        return self.end_time - time()
