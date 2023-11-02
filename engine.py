from langchain.docstore.document import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper
import os
from decouple import config
from default_prompts import preventive_health_urls, prompt_template_cv

from langchain.document_loaders import PyPDFLoader
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI



 #initialize environment keys
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
os.environ["APIFY_API_TOKEN"] = config('APIFY_API_TOKEN')


class DaytwaBot:
    """This is a chat bot, powered by Apify and langchain. 
    Current set to get information from healthline.com. 
    Focused on answering questions related to preventive health.
    """
    def __init__(self):
        # initialize databank, as URL's
        self.urls = preventive_health_urls
        # initilaize apifywrapper
        self.apify = ApifyWrapper()
        
        # Call the Actor to obtain text from the crawled webpages
        self.loader = self.apify.call_actor(
            actor_id="apify/website-content-crawler",
            run_input={"startUrls": self.urls, "maxCrawlPages": 10, "crawlerType": "cheerio"},
            dataset_mapping_function=lambda item: Document(
                page_content=item["text"] or "", metadata={"source": item["url"]}
            ),
        )

        # Create a vector store based on the crawled data
        self.index = VectorstoreIndexCreator().from_loaders([self.loader])

    def query_vector(self, message: str) -> str:
        return self.index.query(message)

class CVAnalytics:
    def summarize(self, cv_path):
        prompt = PromptTemplate.from_template(prompt_template_cv)
        
        # Define LLM chain
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
        llm_chain = LLMChain(llm=llm, prompt=prompt)
    
        loader = PyPDFLoader(cv_path)
        docs = loader.load()
        
        # Define StuffDocumentsChain
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

        summary = stuff_chain.run(docs)
        
        return summary


# # Query the vector store
# query = "What is this lump on my back?"
# result = index.query(query)
# print(result)