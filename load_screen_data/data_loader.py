import immich_integration.api_wrap as immich_integration

def refreshed_buckets():
    raw_list  = immich_integration.get_timeline_buckets()
    items_list = []
    for i in raw_list:
        items_list.append(i["timeBucket"])
    print("rawlist", raw_list)
    return raw_list

