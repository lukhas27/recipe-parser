import os

import firebase_admin

from lib.Parser.eat_this_org import EatThisOrgParser
from lib.firebase_api import CRED, PROJECT_ID, STORAGE_BUCKET
from lib.i_recipe_parser import NotSupportedLinkError

print_path = os.getcwd() + '/Recipes/eat-this-org'

firebase_admin.initialize_app(
    CRED,
    {
        'projectId': PROJECT_ID,
        'storageBucket': STORAGE_BUCKET
    }
)

links = [
    'https://www.eat-this.org/veganes-tzatziki/',
    'https://www.eat-this.org/spanakopita-griechischer-spinatstrudel/',
    'https://www.eat-this.org/vegane-lasagne-bolognese/',
    'https://www.eat-this.org/muhammara-walnuss-paprika-dip/',
    'https://www.eat-this.org/furikake/'
]


def send_to_firestore(link: str):
    parser = None
    try:
        parser = EatThisOrgParser(link)
    except NotSupportedLinkError as e:
        print(e)
        return False

    if parser:
        parser.parse_data()
        parser.save_to_firebase()
        return True
        

def eat_this_org():
    for link in links:
        send_to_firestore(link)


if __name__ == '__main__':
    eat_this_org()
    # scraper = scrape_me('https://www.chefkoch.de/rezepte/779611181045749/Falafel.html')

    # print(scraper)
