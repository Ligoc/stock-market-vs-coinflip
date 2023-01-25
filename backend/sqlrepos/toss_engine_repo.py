class TossEngineRepo:
    '''Test comment'''
    def __init__(self, connection):
        self.connection = connection
        

    def prepare_history_entries(self, history_id, calculations):
        result = []
        for c in calculations:
            result.append((c.start_date, c.calucalted_balance, c.cumulative_difference, history_id))
        return result

    def add_history(self, history):
        sql = ''' INSERT INTO toss_history(`date`, `toss_count`, `index`, `start_date`)
            VALUES(?,?,?,?) '''
        cur = self.connection.cursor()
        cur.execute(sql, history)
        self.connection.commit()
        return cur.lastrowid
    
    def add_history_entries(self, entries_calculated):
        sql = ''' INSERT INTO toss_data(start_date, calucalted_balance, cumulative_difference , history_id)
            VALUES(?,?,?,?) '''
        cur = self.connection.cursor()
        cur.executemany(sql, entries_calculated)
        self.connection.commit()
        
    def get_history_list(self):
        lista = []
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM toss_history order by `date` desc")
        rows = cur.fetchall()
        for row in rows:
            lista.append({'id': row[0], "date_created": row[1], 'count': row[2], 'index': row[3], 'starts_from': row[4]})
        return lista

    def get_history_items(self, history_id):
        lista = []
        cur = self.connection.cursor()
        cur.execute('SELECT * FROM toss_data WHERE history_id = :hid order by `start_date` asc', { 'hid':  history_id})
        rows = cur.fetchall()
        for row in rows:
            lista.append({'id': row[0], 'start_date': row[1], 'calucalted_balance': row[2], 'cumulative_difference': row[3]})
        return lista