import immich_integration.api_wrap as immich_integration

def refreshed_buckets():
    raw_list  = immich_integration.get_timeline_buckets()
    items_list = []
    for i in raw_list:
        items_list.append(i["timeBucket"])
    print("rawlist", raw_list)
    return raw_list

def timebucket_assets_info(timebucket):
    """

    :param timebucket: Time Bucket identifier in YYYY-MM-DD
    :return: timebucket files and size
    """

    timebucket_assets_id = immich_integration.get_timeline_bucket(timebucket)
    assets_info = immich_integration.post_archive_info(timebucket_assets_id)

    return  f"{round(assets_info['totalSize'] / (1024 ** 2), 2)} mb, {len(assets_info['archives'][0]['assetIds'])} archives."
