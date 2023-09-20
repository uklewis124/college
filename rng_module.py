from datetime import datetime

class OscarRNG:
    seed = int(datetime.now().strftime("%S%f")[0:4])

    def next(self,min_num,max_num):
        self.seed = self.seed*self.seed
        str_seed = str(self.seed)
        missing_zeros = 8-len(str_seed)
        for i in range(missing_zeros):
            str_seed = "0" + str_seed
        self.seed = int(str_seed[2:6])
        return min_num + (self.seed % (max_num - min_num))
