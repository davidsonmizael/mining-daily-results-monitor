import gspread

class GoogleSheet:

    def __init__(self, creds) :
        self.creds = creds
        self.client = None

    def authorize(self):
        self.client = gspread.authorize(self.creds)

    def get_sheet(self, name, instance):
        if self.client is None:
            self.authorize()

        sheet =  self.client.open(name) 
        return sheet.get_worksheet(instance)