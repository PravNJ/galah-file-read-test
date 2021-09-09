# Attempt to use SQl to query sobject_ids - dont use this method as the web interface is more efficient 

import numpy as np
import pandas as pd
import requests

#sql_query = "SELECT TOP 100 sobject_id, star_id, teff,e_teff,logg,e_logg, fe_h, e_fe_h FROM galah_dr3.main_star WHERE sobject_id < 160000000000000 and logg < 2.0" #this was the original ADQL query used by brent.miszalski@mq.edu.au
sql_query = "SELECT sobject_id FROM galah_dr3.main_star"
#Query GALAH DR3 catalogue using DataCentral API
api_url = 'https://datacentral.org.au/api/services/query/'
qdata = {'title' : 'get all sobject_ids of GALAH objects', #give a meaningful name
         'notes' : '', #ok if null
         'sql' : sql_query,
         'run_async' : False,
         'email'  : 'prav.nj@gmail.com'}
post = requests.post(api_url,data=qdata).json()
resp = requests.get(post['url']).json() #Python stores this in memory as a dict object
df = pd.DataFrame(resp['result']['data'],columns=resp['result']['columns']) #write to a df