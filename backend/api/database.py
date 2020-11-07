from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    client: AsyncIOMotorClient = None

    async def connect(self):
        self.client = AsyncIOMotorClient('mongodb://localhost:27017')

    async def disconnect(self):
        self.client.close()


db = Database()
