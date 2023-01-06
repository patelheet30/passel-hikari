def open_file(opentype: str):
    file = open("utils/blacklist.txt", mode=opentype)
    return file


def get_ids():
    reader = open_file('r')
    ids = [id.strip() for id in reader]
    return ids[1:]
    
    
def add_ids(id: str):
    lines = get_ids()
    duplicate: bool = False
    if id in lines:
        duplicate = True
    else:
        reader = open_file('a')
        reader.write(f"\n{id}")
    
    return duplicate

def remove_ids(id: str):
    lines = get_ids()
    removed: bool = False
    if id in lines:
        lines.remove(id)
        removed = True
    reader = open_file('w')
    reader.write('blacklist_ids')
    for line in lines:
        reader.write(f"\n{line}")
    
    return removed   
    