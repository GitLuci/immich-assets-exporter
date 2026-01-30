import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

__server_url = os.getenv("SERVER-URL")
__api_key = os.getenv("IMMICH-API-KEY")

# TODO: Filter by asset visibility status (archive, timeline, hidden and locked)
def get_timeline_buckets():
    """
    One list of timeBucket and the number of items in each time bucket
    :return: count : Numb of items, timeBucket : time bucket identifier in YYYY-MM-DD format representing the start of the time period
    """
    request = requests.get(f"{__server_url}/api/timeline/buckets", headers={"x-api-key":__api_key} )
    content = json.loads(request.content)
    return content

def get_timeline_bucket(timeBucket):
    """
    timeBucket : Time bucket identifier in YYYY-MM-DD format (e.g., "2024-01-01" for January 2024)
    :return: Array of asset IDs in the time bucket
    """
    request = requests.get(f"{__server_url}/api/timeline/bucket?timeBucket=%22{timeBucket}%22", headers={"x-api-key":__api_key} )
    content = json.loads(request.content)
    return content["id"]

#TODO: Give the user possibility to download asset by album id
def post_archive_info(assetIds):
    """

    :param assetIds: UUID[]
    :return:  archives : assetIds [], totalSize : Number
    """
    body = {"assetIds":assetIds}
    request = requests.post(f"{__server_url}/api/download/info", headers={"x-api-key":__api_key}, json=body)
    content = json.loads(request.content)
    return content

def post_archive_list(assetIds):
    """

    :param ids_list: UUID[]
    :return: bytes from zip (or rar) file
    """
    body = {"assetIds":assetIds}
    request = requests.post(f"{__server_url}/api/download/archive", headers={"x-api-key":__api_key}, json=body)

    return request.content