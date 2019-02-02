from utils import PropertiesDB
from scrape import perform_scrape    

outcodes = {
            'W6':2766,
            'W14':2748,
            'W8':2768,
            'W2':2762,
            'W12':2746,
            'W10':2744,
            'W11':2745,
            'W9':2769,
            'E14':749,
            'E1':744,
            'E3':756,
            'E2':755,
            'E8':762,
            'E9':763,
            'N1':1666,
            'N5':1683,
            'N16':1673,
            'N7':1685,
            'N4':1682,
            'N19':1676,
            'N6':1684,
            'SW6':2519,
            'SW5':2518,
            'SW2':2514,
            'SW3':2516,
            'SW11':2497,
            'SW18':2504,
            'SW12':2498,
            'SW4':2517,
            'SW9':2522,
            'SW8':2521,
            'SE1':2309,
            'SE11':2311,
            'SE17':2317,
            'SE5':2332,
            'SE15':2315,
            'SE24':2325,
            'SE22':2323,
            'SE16':2316,
            'SE14':2314,
            'SE8':2335,
            'NW1':1855,
            'NW8':1864,
            'NW6':1862,
            'NW3':1859,
            'NW5':1861,

            'SW10':2496,
            'SW7':2520,


            }

regions = {
            'EC1':91983,
            'EC2':91984,
            'EC3':91985,
            'EC4':91986,
            'WC1':91992,
            'WC2':91993,

            'SW1':91989,
            'W1':91991,
             

}


INPUTS = []
for k, v in outcodes.items():
    INPUTS.append({'searchName':k,
    'locationIdentifier': 'OUTCODE^{}'.format(v),
     'radius': 0,
     'maxPrice': 1000000,
     'minPrice': 500000,
     })
    INPUTS.append({'searchName':k,
    'locationIdentifier': 'OUTCODE^{}'.format(v),
     'radius': 0,
     # 'maxPrice': 1000000,
     'minPrice': 1000000,
     })
for k, v in regions.items():
    INPUTS.append({'searchName':k,
    'locationIdentifier': 'REGION^{}'.format(v),
     'radius': 0,
     # 'maxPrice': 1000000,
     'minPrice': 1000000,
     })
    INPUTS.append({'searchName':k,
    'locationIdentifier': 'REGION^{}'.format(v),
     'radius': 0,
     'maxPrice': 1000000,
     'minPrice': 500000,
     })

if __name__ == '__main__':
    conn = PropertiesDB().conn
    perform_scrape(INPUTS, conn)