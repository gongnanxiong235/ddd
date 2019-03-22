from mongoengine import *

connect('tjj_firewall', host='192.168.30.130', port=27017)


class user_property(Document):
    user_id = LongField()
    qcloud_level = IntField()
    qcloud_risk_type = ListField()

    def __str__(self):
        return str(self.qcloud_level)
