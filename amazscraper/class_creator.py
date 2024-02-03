import time 

base_script = '''
from langchain_core.pydantic_v1 import BaseModel, Field

class _Response(BaseModel):
'''
def create_class(data_dict: dict):
    '''
    This function creates a class at runtime using the values from the list.
    Parameters:
        data_dict 
            dict {
                "title": str
                "type": str,
                "description": str
            }: dictionary for describing the  prompt
    '''
    for elem in data_dict:
        global base_script
        base_script = base_script + f"    {elem['title']}: {elem['type']} = Field(description='{elem['description']}')\n"

    with open("./amazscraper/pydantic_class.py", "w") as f:
        f.write(base_script)