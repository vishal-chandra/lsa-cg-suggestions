import requests
from requests.structures import CaseInsensitiveDict
import json

sessions = ["Winter", "Spring", "Sp/Su", "Summer", "Fall"]
reference_term = ("Winter", 2022, 2370) #(term, year, term_id)

def get_term_id(session, year):
    base_term_id = reference_term[2] 
    base_term_id -= (reference_term[1] - year) * len(sessions) * 10
    
    term_id_offset = sessions.index(session) * 10
    corrected_term_id = base_term_id + term_id_offset
    return corrected_term_id

def get_cg_autocomplete(session, year, input, count=20):
    term_id = get_term_id(session, year)

    url = "https://www.lsa.umich.edu/cg/default.aspx/SearchCourseOfferings"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
    "prefixText":input,
    "count":count,
    "contextKey":str(term_id) + "|ug"
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))

    return resp.json()

