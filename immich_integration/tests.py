import api_wrap

errors = 0
success = 0
trys = 0

def test_score(err,succ):
    global trys,errors,success
    trys += 1
    if err == 1:
        errors += 1
    elif succ == 1:
        success += 1

# First Test: retrieve timeBuckets list
try:
    time_line_buckets = api_wrap.get_timeline_buckets()
    test_score(0,1)
except Exception as exp:
    print("Error :  get time_line_buckets test. ", exp)
    test_score(1,0)


# Secont Test: From a random timeBuckets, retrieve Assets UUID
try:
    time_line_bucket = api_wrap.get_timeline_bucket(time_line_buckets[-1]["timeBucket"])
    test_score(0,1)
except Exception as exp:
    print("Error :  get time_line_bucket test. ", exp)
    test_score(1,0)

# Third Test: get assets info
try:
    assets_raw_info = api_wrap.post_archive_info(time_line_bucket)
    test_score(0,1)
except Exception as exp:
    print("Error :  post_archive_info test. ", exp)
    test_score(1,0)


# Fourth Test: Download and save archives
try:
    print("Attention: If the terminal looks like is freeze, probably isn't, turn on the tests prints to see the assets file size and if needed, change the time bucket for a minor one")
    raw_bytes = api_wrap.post_archive_list(assets_raw_info['archives'][0]['assetIds'])
    with open("test_file.zip","wb") as f:
        f.write(raw_bytes)

    test_score(0,1)
except Exception as exp:
    print("Error :  post_archive_list test. ", exp)
    test_score(1,0)




print(f"Total trys {trys}, total success {success}, total errors {errors}")
