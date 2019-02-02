import requests
import os
from datetime import datetime
import logging
import time

print(os.path.realpath(__file__))

TABLE = os.environ.get('TABLE')
URL = os.environ.get('URL')
PER_PAGE = 499

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
log_path_ext = f'/logs/log_{datetime.today().strftime("%Y_%m_%d_%H_%M")}.log'
log_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) +  log_path_ext
handler = logging.FileHandler(log_path)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def generate_payload(input):
    payload = input.copy()
    payload['includeSSTC'] = 'true'
    payload['viewType'] = 'LIST'
    payload['channel'] = 'BUY'
    payload['areaSizeUnit'] = 'sqft'
    payload['currencyCode'] = 'GBP'
    payload['isFetching'] = 'false'
    return payload

def get_page_of_properties(payload, index):
    params = payload
    params['numberOfPropertiesPerPage'] = PER_PAGE
    params['index'] = index
    return requests.get(URL, params=params).json()['properties']

def get_pages(payload):
    params = payload
    params['numberOfPropertiesPerPage'] = PER_PAGE
    response = requests.get(URL, params=params).json()
    pages = response['pagination']['options']
    return pages

def get_all_properties_for_payload(payload, delay=3):
    pages = get_pages(payload)
    logger.info(f'Total number of pages: {len(pages)}')
    properties_list = []
    for page in pages:
        logger.info(f'Collecting page: {page["description"]}')
        params = payload.copy()
        properties = get_page_of_properties(payload, page['value'])
        properties_list.extend(properties)
        time.sleep(delay)
    return properties_list


class Property(object):
    def __init__(self, id):
        self.id = id
        self.retrieved_at = datetime.today().date()

    def __repr__(self):
        return f"Property: id={self.id}"

    def write_to_db(self, db_conn):
        cur = db_conn.cursor()
        d = self.__dict__
        keys = d.keys()
        columns = ','.join(keys)
        values = ','.join(['%({})s'.format(k) for k in keys])
        insert = 'insert into {0} ({1}) values ({2})'.format(TABLE, columns, values)
        cur.execute(cur.mogrify(insert, d))
        db_conn.commit()
        return self

def parse_date(str):
    return datetime.strptime(str[:10], '%Y-%m-%d').date()

def parse_property(p_dict):
    p = Property(id=p_dict['id'])
    p.price = p_dict['price']['amount']
    p.bedrooms = p_dict['bedrooms']
    p.display_address = p_dict['displayAddress']
    p.lat = p_dict['location']['latitude']
    p.lon = p_dict['location']['longitude']
    p.update_reason = p_dict['listingUpdate']['listingUpdateReason']
    p.update_date = parse_date(p_dict['listingUpdate']['listingUpdateDate'])
    p.premium_listing = p_dict['premiumListing']
    p.featured_property = p_dict['featuredProperty']
    p.display_price_qualifier = p_dict['price']['displayPrices'][0]['displayPriceQualifier']
    p.property_subtype = p_dict['propertySubType']
    p.branch_id = p_dict['customer']['branchId']
    p.branch_name = p_dict['customer']['brandTradingName']
    p.development = p_dict['development']
    p.first_visible_date = parse_date(p_dict['firstVisibleDate'])
    p.url = p_dict['propertyUrl']
    p.summary = p_dict['summary']
    p.display_status = p_dict['displayStatus']
    return p

def perform_scrape(inputs, db_conn, delay=300):
    logger.info('Starting scrape')
    scraped_ids = []
    payloads = [generate_payload(i) for i in inputs]
    for pl in payloads:
        try:
            logger.info(f"Scraping search: {pl['searchName']}")
            prop_list = get_all_properties_for_payload(pl)
        except Exception as e:
            logger.error(f"Problem scraping {pl['searchName']}", exc_info=True)

        for prop in prop_list:
            if prop['id'] in scraped_ids:
                logger.info(f"Passing property {prop['id']} as it has already been processed")
                continue
            try:
                p_save = parse_property(prop)
                p_save.search_name = pl['searchName']
                p_save.write_to_db(db_conn)
                scraped_ids.append(p_save.id)
            except Exception as e:
                logger.error(f"Problem saving {prop['id']}", exc_info=True)
        time.sleep(delay)
    logger.info('Finished scrape')



