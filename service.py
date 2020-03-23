# -*- coding: utf-8 -*-
import csv
import json
import logging
import re
from itertools import zip_longest

import boto3
import requests
from botocore.exceptions import ClientError

BUCKET = "trade-leads"
KEY = "ustda.json"
JSON = "application/json"
ENDPOINT = "https://buyandsell.gc.ca/procurement-data/csv/tender/active"
REGEXP = re.compile(r", ([0-9A-Z]+ -)")
S3_CLIENT = boto3.client("s3")


def handler(event, context):
    entries = get_entries()
    response = True
    try:
        S3_CLIENT.put_object(
            Bucket=BUCKET, Key=KEY, Body=json.dumps(entries), ContentType=JSON
        )
        print(f"✅ Uploaded {KEY} file with {len(entries)} locations")
    except ClientError as e:
        logging.error(e)
        response = False
    return response


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def split_industries(gsin):
    regex_split = re.split(REGEXP, gsin)
    segments = [regex_split.pop(0)]
    industries = segments + [" ".join([a, b]) for a, b in grouper(2, regex_split)]
    return " | ".join(industries)


def process_entry(lead):
    lead["gsin"] = split_industries(lead.get("gsin", ""))
    lead.pop(None, None)
    return lead


def get_entries():
    print(f"Fetching CSV feed of items from {ENDPOINT}...")
    response = requests.get(ENDPOINT)
    response.encoding = response.apparent_encoding
    reader = csv.DictReader(response.text.splitlines())
    items = [process_entry(row) for row in reader if row["language"] == "English"]
    print(f"Found {len(items)} items in {ENDPOINT}")
    return items
