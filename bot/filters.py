from telegram.ext.filters import MessageFilter

class TextFilter(MessageFilter):
    def filter(self, message):
        return message.text is not None

text_filter = TextFilter()
