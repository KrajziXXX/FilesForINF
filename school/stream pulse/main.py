#funkcja wczytujaca dane z pliku
def loaddata(filename):
    import os
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as file:
        data = file.readlines()
    return [line.strip() for line in data]

#funkcja wyświetlająca tablice w tablicy ascii
def displaydata(data):
    print("TIME  | CONTENT | CAT   | VIEWS | LIKES | COM | SHR")
    print("--------------------------------------------------------")
    for row in data:
        print(row.replace(";", " | "))

#filtrowanie filter_type = category/content_id/min_views
def filterdata(data, filter_type, value):
    if filter_type == "category":
        return [row for row in data if row.split(";")[2] == value]
    elif filter_type == "content_id":
        return [row for row in data if row.split(";")[1] == value]
    elif filter_type == "min_views":
        return [row for row in data if int(row.split(";")[3]) >= value]
    else:
        return []

#analiza każdego rekordu oraz wyswietlanie w tabeli asci z dodatkowym headem STATUS, możliwość kilku tagów
def anliz(data):
    new_tab = []
    for row in data:
        time, content, cat, views, likes, com, shr = row.split(";")
        views = int(views)
        likes = int(likes)
        com = int(com)
        shr = int(shr)
        tags = []
        if views > 3000:
            tags.append("TRENDING")
        if shr > 10:
            tags.append("VIRAL")
        if com > 100:
            tags.append("ENGAGING")
        new_row = f"{time};{content};{cat};{views};{likes};{com};{shr};{','.join(tags) if tags else 'NORMAL'}"
        new_tab.append(new_row)
    print("TIME | CONTENT | CAT | VIEWS | LIKES | COM | SHR | STATUS")
    print("-" * 70)
    for row in new_tab:
        print(row.replace(";", " | "))
    return new_tab

#funkcja main
def main():
    tab = loaddata("streams.txt")
    print("Data:")
    displaydata(tab)
    print("\nfilter by content_id:")
    displaydata(filterdata(tab, "content_id", "VID_001"))
    print("\nfilter by category:")
    displaydata(filterdata(tab, "category", "Gaming"))
    print("\nfilter by min_views:")
    displaydata(filterdata(tab, "min_views", 2000))
    print("\nAnalysis:")
    anliz(tab)

main()
