import json
import pandas as pd
import urllib.request
import numpy as np
import time
from datetime import timedelta
import pickle

class FX_API(object):

    def __init__(self, startdate, enddate, base):
        self.base = base
        self.startdate = startdate
        self.enddate = enddate
        url = 'https://api.fixer.io/' + startdate + '?base=' + self.base
        opem1 = urllib.request.urlopen(u)
        r1 = opem1.read()
        opem1.close()
        data = json.loads(r1.decode())
        cols = sorted(list(data['rates'].keys()))
        num_days = pd.bdate_range(startdate, enddate)

        df = pd.DataFrame(columns=cols + ['date'], index=range(len(num_days)))
        date = datetime.strptime(startdate, '%Y-%m-%d')
        for i in range(len(num_days)):

            date1 = datetime.strftime(date, '%Y-%m-%d')
            df['date'] = date1
            D = GetD_cols(date1)
            for col in cols:
                df['col'] = D['rate']['col']
            date += time.delta(days=1)



    def GetD_cols(self, date):
        u = 'https://api.fixer.io/' + date + '?base=' + self.base
        opem = urllib.request.urlopen(u)
        r = opem.read()
        opem.close()
        d = json.loads(r.decode())
        return d

    def save_data(self):
        file_name = self.base_self.startdate_self.enddate
        name = file_name.pickle
        pickle_out = open('name', 'wb')
        pickle.dump(df, pickle_out)
        pickle_out.close()
        
