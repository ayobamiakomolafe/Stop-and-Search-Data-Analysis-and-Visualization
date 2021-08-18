"This module extracts the data"
'''
Since we need to get the data through the stop and search by force API which is dependent on
force IDs, first we need to get the list of force IDs via
the API: https://data.police.uk/api/forces  '''


# **DATA GATHERING VIA API**

'Import Libraries'
def data_extraction():
    
    from urllib.request import urlopen
    import json as js
    html='https://data.police.uk/api/forces'  # Html to the force API
    html_request=urlopen(html)
    force_id=html_request.read()
    force_ids=js.loads(force_id)              # Load the returned force_ids into a json object
    ids=list()
    for id in force_ids:
        id=id['id']
        ids.append(id)

    """Haven gotten the force ids, we can proceed to get the stop and search data for the respective force ids. The data collected
    is for the month of March 2021, hence we set date params as 2021-03"""

    base_url='https://data.police.uk/api/stops-force?'

    from urllib.parse import urlencode

    'Create a list to store all the data as they are being collected'

    age_range=list()
    self_defined_ethnicity=list()
    outcome_linked_to_object_of_search=list()
    datetime=list()
    removal_of_more_than_outer_clothing=list()
    operation=list()
    officer_defined_ethnicity=list()
    object_of_search=list()
    involved_person=list()
    gender=list()
    legislation=list()
    location=list()
    outcome=list()
    type_=list()
    operation_name=list()
    force_ids=list()

    'we loop through each of the force_id and collect their stop and search by force data for the month of march'


    for id in ids:
        params=dict()                                     
        params['force']=id  
        params['date']='2021-03'                            
        service_url=urlencode(params)                   
        url=base_url+service_url
        'Many times a 500 Server error is returned due to errors from their server, a try and except as been used to catche this'
        try:
            html_stop_searches=urlopen(url)
        except:
            continue 
        stop_searches=html_stop_searches.read()
        js_stop_searches=js.loads(stop_searches)         

     

        for js_stop_search in js_stop_searches:
            force_ids.append(id)
            age_range.append(js_stop_search['age_range'])
            self_defined_ethnicity.append(js_stop_search['self_defined_ethnicity'])
            outcome_linked_to_object_of_search.append(js_stop_search['outcome_linked_to_object_of_search'])
            datetime.append(js_stop_search['datetime'])
            removal_of_more_than_outer_clothing.append(js_stop_search['removal_of_more_than_outer_clothing'])
            officer_defined_ethnicity.append(js_stop_search['officer_defined_ethnicity'])
            object_of_search.append(js_stop_search['object_of_search'])
            involved_person.append(js_stop_search['involved_person'])
            gender.append(js_stop_search['gender'])
            legislation.append(js_stop_search['legislation'])
            location.append(js_stop_search['location'])
            outcome.append(js_stop_search['outcome'])
            type_.append(js_stop_search['type'])
            operation_name.append(js_stop_search['operation_name'])
            operation.append(js_stop_search['operation'])

    """Create a dictionary of data names and column names to create a pandas dataframe"""

    data={'age_range':age_range,
    'self_defined_ethnicity':self_defined_ethnicity,
    'outcome_linked_to_object_of_search':outcome_linked_to_object_of_search,
    'datetime':datetime,
    'removal_of_more_than_outer_clothing':removal_of_more_than_outer_clothing,
    'operation':operation,
    'officer_defined_ethnicity':officer_defined_ethnicity,
    'object_of_search':object_of_search,
    'involved_person':involved_person,
    'gender':gender,
    'legislation':legislation,
    'location':location,
    'outcome':outcome,
    'type_':type_,
    'operation_name':operation_name,
    'force_ids':force_ids}

    import pandas as pd

    global df
    df=pd.DataFrame(data)
    
    


