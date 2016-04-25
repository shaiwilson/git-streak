
import json
import requests
import argparse


# todo put the oauth token in seperate secrets.sh file
API_TOKEN = 'SECRET_TOKEN'
url = "https://api.github.com/users/"

HEADERS = {
        'Authorization': 'token %s' % API_TOKEN
}

# class GitHub(object):

#     def __init__(self, **config_options):
#         self.__dict__.update(**config_options)
#         self.session = requests.Session()
#         self.header = {'X-Github-Username': self.username,
#                'X-Github-API-Token': self.api_token                  
#         }

#         if hasattr(self, 'api_token'):
#            self.session.headers['Authorization'] = 'token %s' % self.api_token
#         elif hasattr(self, 'username') and hasattr(self, 'password'):
#            self.session.auth = (self.username, self.password)

#     def call_to_the_api(self, *args):
#         # do stuff with args
#         return self.session.post(url)

def main():

    parser = argparse.ArgumentParser(description='List Github repositories.')
    parser.add_argument('-t', '--type', 
        nargs = 1,
        dest = 'type',
        default = 'all',
        metavar = 'TYPE',
        help = 'What type of repos to list',
        )

    args = parser.parse_args() 

    res = requests.get(url + API_TOKEN, headers=HEADERS)
    data = json.loads(res.text)
    jsonList = []
    jsonList.append(json.loads(res.content))
    print jsonList

    
if __name__ == '__main__':
    main()