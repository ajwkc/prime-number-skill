from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class PrimeNumber(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('number.prime.intent')
    def handle_number_prime(self, message):
        self.speak_dialog('number.prime')


def create_skill():
    return PrimeNumber()

