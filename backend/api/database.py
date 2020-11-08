from motor.motor_asyncio import AsyncIOMotorClient
import pandas as pd
import string


class Database:
    client: AsyncIOMotorClient = None

    async def connect(self):
        self.client = AsyncIOMotorClient('mongodb://localhost:27017')

        if await db.client.unigrams.get_collection('a').find_one() == None:
            # Parse data
            print("generating database...")
            unigrams = pd.read_csv('./api/data/count_1w.txt', index_col=0, delimiter='\t', header=None)
            for c in string.ascii_lowercase:
                lettered = unigrams.filter(regex='^'+c, axis=0).head(100)
                self.client.unigrams.get_collection(c).insert_many(
                    [{'word':index, 'count':int(row.iloc[0])} for index, row in lettered.iterrows()] 
                )

    async def disconnect(self):
        self.client.close()

db = Database()

