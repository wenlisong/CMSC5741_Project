import os


def parse_prefix(img_name):
    prefix = ''
    if img_name and img_name.split('_'):
        prefix = img_name.split('_')[0]
    return prefix


names_dir = "../../data/names/"
count = 0
save_count = 0
datastore = {}
for file in os.listdir(names_dir):
    with open(os.path.join(names_dir, file), encoding='ISO-8859-1') as f:
        # item example: nm0000001_rm124825600_1899-5-10_1968.jpg,Fred Astaire
        for item in f:
            data = item.split(',')
            if len(data) >= 2:
                prefix = parse_prefix(data[0])
                if prefix not in datastore:
                    name = data[1].rstrip()
                    datastore[prefix] = name
                    save_count += 1
                count += 1
                if count % 1000 == 0:
                    print("save_count=%d, total_count=%d" % (save_count, count))
            else:
                print("error on item=%s" % item)
    print("process %s done." % file)
# process all done with 523051 items, save_count=82654.
print("process all done with %d items, save_count=%d." % (count, save_count))
