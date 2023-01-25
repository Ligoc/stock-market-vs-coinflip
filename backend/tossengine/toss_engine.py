import csv, os, random, json
from datetime import datetime, date


class TossEngine2:
    def __init__(self):
        self.file_name = ""
        self.day_results = []

    def run_engine(self, start_date, toss_number, index_name):
        self.fix_csv_header(index_name)
        self.day_results = self.read_csv_file(start_date, toss_number)
        self.apply_random_coin_toss()
        self.calculate_win_lose()
        self.calculate_cumulative_balances()
        return self.day_results  #self.to_json()
    
    def fix_csv_header(self, index_name):
        self.file_name = f"backend/stock_market_files/{index_name}_d.csv"
        row_found = False
        serch_row = "Date,Open,High,Low,Close,Volume"
        print(os.getcwd())
        stooq_file = open(self.file_name, "r")
        temp_file = open(f"backend/stock_market_files/temp_{index_name}.txt", "w")
        data_csv = stooq_file.readline()
        while data_csv != "":
            data_csv = data_csv.rstrip('\n')
            if data_csv != serch_row:
                temp_file.write(data_csv + '\n')
            else:
                row_found = True
            data_csv = stooq_file.readline()
        stooq_file.close()
        temp_file.close()   
        os.remove(self.file_name)
        os.rename(f"backend/stock_market_files/temp_{index_name}.txt", self.file_name)
        if row_found:
            print("Data was up-to-date.")
        else:
            print("Data don't need to be updated.")
    
    def read_csv_file(self, start_date, toss_count):
        with open(self.file_name) as f:
            result = []
            current_count = 0
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            reader = csv.reader(f)
            for row in reader:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                if (current_date >= start_date) and (current_count < toss_count):
                    try:
                        opening_value = float(row[1])
                        closing_value = float(row[4])
                    except ValueError:
                        print(f"Missing data for {current_date}")
                    else:
                        difference_val = closing_value - opening_value
                        result.append(TossResult(current_date, opening_value, closing_value, difference_val, 0, 0, 0))

                    current_count+=1
            return result
    
    def apply_random_coin_toss(self):
        for r in self.day_results:
            r.coin_toss = random.randint(0,1)

    def calculate_win_lose(self):
        for r in self.day_results:
            index = self.day_results.index(r)
            if index == 0:
                if r.coin_toss == 1:
                    r.calucalted_balance = float(r.difference)
                if r.coin_toss == 0:
                    r.calucalted_balance = -float(r.difference)
            else:
                prev = self.day_results[index-1]
                if r.coin_toss == 1:
                    r.calucalted_balance = prev.calucalted_balance + float(r.difference)
                if r.coin_toss == 0:
                    r.calucalted_balance = prev.calucalted_balance -float(r.difference)

    def calculate_cumulative_balances(self):
        for r in self.day_results:
            index = self.day_results.index(r)
            if index == 0:
                r.cumulative_difference = float(r.difference)
            else:
                prev = self.day_results[index-1]
                r.cumulative_difference = prev.cumulative_difference + float(r.difference)

   

    def to_json(self, results):
        return json.dumps([ob.__dict__ for ob in results], default=str)
        
        

class TossResult:
    # def __new__(cls, *args):
    #     new_toss_result = object.__new__(cls)
    #     print("TossResult __new__ gets called")
    #     print(f"TossResult Instance Memory Address: {id(new_toss_result)}")
    #     return new_toss_result

    def __init__(self, start_date, open, close, difference, coin_toss, calucalted_balance, cumulative_difference):
        #isinstance(startDate, type(datetime))
        # print(self.__dict__)
        self.start_date = start_date
        self.open = open
        self.close = close
        self.difference = difference
        self.coin_toss = coin_toss
        self.calucalted_balance = calucalted_balance
        self.cumulative_difference = cumulative_difference
        # print("TossResult __init__ gets called")
        # print(f"Set Initial State: {id(self)}")
        # print(self.__dict__)
        # print()
    
    # def __del__(self):
        # print(f"The object is getting deleted: {self}")

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, 
    #         sort_keys=True, indent=4)

