from redcap import Project

api_url = 'https://redcap.vanderbilt.edu/api/'

hospitalized_key = open("key.txt").read()
hospitalized_proj = Project(api_url, hospitalized_key)
hospitalized_raw = hospitalized_proj.export_records(format='df', 
                            df_kwargs={'index_col': hospitalized_proj.field_names[0]})
print(hospitalized_raw.head())
print(hospitalized_raw.columns)
hospitalized_raw.to_csv("kawasaki.csv")
import pandas as pd
pd.Series(hospitalized_raw.columns).to_csv('fields.csv')

metadata = hospitalized_proj.export_metadata()
print(metadata)

def get_field(name):
    f = [rec for rec in metadata if rec['field_name']==name][0]
    print(f)
    
get_field('echo_2')