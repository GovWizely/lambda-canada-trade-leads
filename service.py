# -*- coding: utf-8 -*-
import csv
import json
import re
from itertools import izip_longest

import boto3
import requests

ENDPOINT = 'https://buyandsell.gc.ca/procurement-data/csv/tender/active'
REGEXP = re.compile(r', ([0-9A-Z]+ -)')

s3 = boto3.resource('s3')


def handler(event, context):
    items = get_items()
    if len(items) > 0:
        s3.Object('trade-leads', 'canada.json').put(Body=json.dumps(items),
                                                    ContentType='application/json')
        return "Uploaded canada.json file with %i locations" % len(items)
    else:
        return "No entries loaded so there is no JSON file to upload"


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def split_industries(gsin):
    regex_split = re.split(REGEXP, gsin)
    segments = [regex_split.pop(0)]
    industries = segments + [' '.join([a, b]) for a, b in grouper(2, regex_split)]
    return ' | '.join(industries)


def process_entry(lead):
    lead['gsin'] = split_industries(lead.get('gsin', ''))
    lead.pop(None, None)
    return lead


def get_items():
    print "Fetching CSV feed of items from {}...".format(ENDPOINT)
    response = requests.get(ENDPOINT)
    response.encoding = 'UTF-8-SIG'
    reader = csv.DictReader(response.text.encode('utf-8').splitlines())
    items = [process_entry(row) for row in reader if row['language'] == 'English']
    print "Found {} items in {}".format(len(items), ENDPOINT)
    return items
