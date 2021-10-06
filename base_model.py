class BaseModel:
    def __init__(self, id=None):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def describeMe(self):
        print('This is the base model for Ad and Advertiser classes.')

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_views(self):
        self.__views += 1

    def inc_clicks(self):
        self.__clicks += 1
