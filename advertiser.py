from base_model import BaseModel


class Advertiser(BaseModel):
    __total_clicks = 0

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def inc_clicks(self):
        super().inc_clicks()
        Advertiser.__total_clicks += 1

    def describeMe(self):
        print('This class contains fields and methods for system advertisers.')

    @staticmethod
    def get_total_clicks():
        return Advertiser.__total_clicks

    @staticmethod
    def help():
        print("id: This unique field keep the id of advertiser in a int variable.\n" +
              "name: This field is name of advertiser and sort in String.\n" +
              "clicks: This field save the count of clicks of advertiser.\n" +
              "views: This field keep the count of views of advertiser.")
