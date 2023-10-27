from langchain.docstore.document import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper
import os
from decouple import config
from default_prompts import preventive_health_urls

class DaytwaBot:
    """This is a chat bot, powered by Apify and langchain. 
    Current set to get information from healthline.com. 
    Focused on answering questions related to preventive health.
    """
    def __init__(self):
        #initialize environment keys
        os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
        os.environ["APIFY_API_TOKEN"] = config('APIFY_API_TOKEN')
        
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




# # Query the vector store
# query = "What is this lump on my back?"
# result = index.query(query)
# print(result)