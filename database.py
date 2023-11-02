import chromadb
import os

import logging
import chromadb
import os
from utils import Utilities
import utcnow

# Initialize the utilities helper
utilities = Utilities()

class Vectorizer:
    def __init__(self, user_id, data_type) -> None:
        self.working_dir = os.getcwd()
        self.unique_username = f"profile_{user_id}"
        self.client = chromadb.PersistentClient(path=f"{self.working_dir}/{data_type}/{self.unique_username}")
        self.user_id = user_id

    def store_cv_summary(self, summary: str) -> None:
        """Training program method responsible for, evaluating cv and suggesting relevant training programme.
        Sotres vectorized user cv summary.
        """
        collection = self.client.get_or_create_collection(name=self.unique_username)

        collection.add(
            documents=[summary,],
            metadatas=[
                {"date": utcnow.get()},],
            ids=[str(self.user_id),]
        )
        print('success!!')
        return 0

    def get_cv_summary(self):
        collection = self.client.get_or_create_collection(name=self.unique_username)
        results = collection.get(
            ids=[str(self.user_id),]
            )
        if len(results['ids']) == 0:
            # If there is no subscription data
            print('No Summary Found')
            return 0
        
        if len(results['ids']) > 1:
            print('Error: Multiple entries found on user.')
            return 1
            
        if len(results['ids']) == 1:
            try:
                summary = results['documents'][0]
            except KeyError:
                print('For some reason the key is not in metadatas')
                
            return summary

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
        