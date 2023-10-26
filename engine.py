from langchain.docstore.document import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper
import os
from decouple import config

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
        self.urls = [
            {'url': 'https://www.healthline.com/search?q1=Preventive%20Health'}, {'url': 'https://www.healthline.com/search?q1=Wellness'}, 
            {'url': 'https://www.healthline.com/search?q1=Preventive%20Medicine'}, {'url': 'https://www.healthline.com/search?q1=Health%20Tips'}, 
            {'url': 'https://www.healthline.com/search?q1=Disease%20Prevention'}, {'url': 'https://www.healthline.com/search?q1=Healthy%20Lifestyle'}, 
            {'url': 'https://www.healthline.com/search?q1=Immunizations'}, {'url': 'https://www.healthline.com/search?q1=Nutrition'}, 
            {'url': 'https://www.healthline.com/search?q1=Physical%20Activity'}, {'url': 'https://www.healthline.com/search?q1=Stress%20Reduction'}, 
            {'url': 'https://www.healthline.com/search?q1=Mental%20Health'}, {'url': 'https://www.healthline.com/search?q1=Preventive%20Screenings'}, 
            {'url': 'https://www.healthline.com/search?q1=Healthy%20Aging'}, {'url': 'https://www.healthline.com/search?q1=Family%20Health'}, 
            {'url': 'https://www.healthline.com/search?q1=Community%20Health'}]
        
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