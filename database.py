__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb
import os

class Profiler:
    def __init__(self, user_id) -> None:
        self.working_dir = os.getcwd()
        self.unique_username = f"profile_{user_id}"
        self.client = chromadb.PersistentClient(path=f"{self.working_dir}/profiles/{self.unique_username}")
        self.user_id = user_id

    def store_profile(self, data: tuple) -> None:
        """Profiler method responsible for 
        1. Storing vectorized user health data. This information is gotten from chats.
        2. querying the user healt data and augmenting prompt.
        """
        question, answer = data
        collection = self.client.get_or_create_collection(name=self.unique_username)
        
        collection.add(
            documents=[answer,],
            metadatas=[{"user_id": self.user_id},],
            ids=[question,]
        )
        print('success!!')
        return 0

    def retrieve_profile(self, data: str):
        """Profiler method responsible for 
        1. Checking a users vectorized health data and returning a prompt relevent to the query.
        This information is gotten from chats.
        """
        collection = self.client.get_or_create_collection(name=self.unique_username)
        results = collection.query(
            query_texts=[data],
            n_results=1
        )
        question = results['ids'][0][0]
        answer = results['documents'][0][0]
        print('success!!')
        return question, answer
        