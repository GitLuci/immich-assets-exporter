import immich_integration.api_wrap as immich_integration


def timebucket_assets_download(timebucket):
    """

    :param timebucket: Time Bucket identifier in YYYY-MM-DD
    :return: assets bytes
    """
    timebucket_assets_id = immich_integration.get_timeline_bucket(timebucket)
    assets_info = immich_integration.post_archive_info(timebucket_assets_id)
    assets_bytes = immich_integration.post_archive_list(assets_info['archives'][0]['assetIds'])
    return assets_bytes
