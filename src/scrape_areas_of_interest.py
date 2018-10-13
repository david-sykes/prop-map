from utils import PropertiesDB
from scrape import perform_scrape    

INPUTS = (
    {'searchName':'Camberwell 2+ Beds',
    'locationIdentifier': 'REGION^70440',
     'radius': 0.25,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'De Beauvoir 2+ Beds',
    'locationIdentifier': 'REGION^70393',
     'radius': 0.25,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Vauxhall 2+ Beds',
    'locationIdentifier': 'REGION^70424',
     'radius': 0.25,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Brixton 2+ Beds',
    'locationIdentifier': 'REGION^87496',
     'radius': 0.25,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Highbury 2+ Beds',
    'locationIdentifier': 'REGION^70438',
     'radius': 0.5,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Muswell Hill 2+ Beds',
    'locationIdentifier': 'REGION^85376',
     'radius': 0.5,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Kentish Town 2+ Beds',
    'locationIdentifier': 'REGION^85230',
     'radius': 0.5,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},
    {'searchName':'Battersea 2+ Beds',
    'locationIdentifier': 'REGION^87492',
     'radius': 0.0,
     'maxPrice': 750000,
     'minPrice': 500000,
     'minBedrooms':2},

     


)


if __name__ == '__main__':
    conn = PropertiesDB().conn
    perform_scrape(INPUTS, conn)