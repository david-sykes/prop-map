from utils import PropertiesDB
from scrape import perform_scrape    

INPUTS = (
    {'searchName':'N1',
    'locationIdentifier': 'OUTCODE^1666',
     'radius': 0,
     'maxPrice': 750000,
     'minPrice': 500000,
     },
    {'searchName':'N5',
    'locationIdentifier': 'OUTCODE^1683',
     'radius': 0,
     'maxPrice': 750000,
     'minPrice': 500000,
     },
    {'searchName':'N7',
    'locationIdentifier': 'OUTCODE^1685',
     'radius': 0,
     'maxPrice': 750000,
     'minPrice': 500000,
     },
    {'searchName':'N19',
    'locationIdentifier': 'OUTCODE^1676',
     'radius': 0,
     'maxPrice': 750000,
     'minPrice': 500000,
     },
)


if __name__ == '__main__':
    conn = PropertiesDB().conn
    perform_scrape(INPUTS, conn)