from syncsketch import SyncSketchAPI
from dotenv import load_dotenv
import os

class SyncSketch:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv("SYNCSKETCH_SCRIPT_USER_ACCOUNT")
        self.api_key = os.getenv("SYNCSKETCH_SCRIPT_USER_APP_API")
        self.s = SyncSketchAPI(self.username, self.api_key)

#     Verify your credentials work
    def test_connection(self):
        print(self.s.is_connected())
        #Display your current user data
        #print(s.get_current_user())x

    def get_users(self):
        print(self.s.getUsersByName('Chris', fields= "full_name",raw_response=False))

    def print_projectList(self):
        print(self.s.get_projects(fields=['name','id']))
    
    def print_userList(self):
        pass

testing = SyncSketch()
# testing.test_connection()
#testing.print_projectList()
testing.get_users()