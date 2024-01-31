from dotenv import load_dotenv
from .pydantic_class import _Response
from .class_creator import create_class
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import Field
from langchain.output_parsers import PydanticOutputParser

class Generator:
    def __init__(self, values:list, api_key:str, temperature_param:float = 0, model_name:str = "gpt-3.5-turbo"):
        """
        Initializes the Generator object.

        Parameters:
        - values (list): A list of values used for class creation.
        - temperature_param (float): A parameter controlling the randomness of the language model's output.
        - model_name (str): The name of the language model to be used (default: "gpt-3.5-turbo"). All
          the possible models are avaible at the following link: https://platform.openai.com/docs/models

        Returns:
        - result_dict (dict): The result of the language model invocation, converted to a dictionary.
        """
        create_class(values)

        self.parser = PydanticOutputParser(pydantic_object=_Response)

        self.prompt = PromptTemplate(
            template="Answer the user query.\n{format_instructions}\n{query}\n",
            input_variables=["query"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()},
        )

        self.model = ChatOpenAI(openai_api_key=api_key, temperature=temperature_param, model=model_name)

        self.chain = self.prompt | self.model | self.parser

    def invocation(self, query_info):
        try:
            result = self.chain.invoke({"query": query_info})
            result_dict = result.dict()  
            
            return result_dict
        except Exception as e:
            print(f"Error: {e}")
