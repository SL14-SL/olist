import os
import pandas as pd

class Olist:
    def get_data(self):
        '''
        This function returns a python dict, in which all the data from the nine
        csv-files is stored.
        Keys are: 'sellers', 'orders', 'order_items', ...
        Values are dataframes
        '''

        root_path = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_path,'raw_data')
        full_path = os.listdir(path=csv_path)

        file_names = []
        for i in full_path:
            if i.endswith('.csv'):
                file_names.append(i)
        key_names = []
        for name in file_names:
            name = name.replace(".csv","")
            name = name.replace("_dataset", "")
            name = name.replace("olist_", "")
            key_names.append(name)
        data = {}
        for (name, key_name) in zip(file_names,key_names):
            file_path = f"{csv_path}/{name}"
            df = pd.read_csv(file_path)
            data[key_name]  = df

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
