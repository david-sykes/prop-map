from utils import PropertiesDB
from scrape import perform_scrape    

INPUTS = (
    {'searchName':'SW11',
    'locationIdentifier': 'OUTCODE^2497',
     'radius': 0,
     'maxPrice': 750000,
     'minPrice': 500000},
   

     


)


if __name__ == '__main__':
    conn = PropertiesDB().conn
    perform_scrape(INPUTS, conn)