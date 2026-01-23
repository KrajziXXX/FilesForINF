# Autor: Krystian Wyrwicki

#Importy
import os

#Funkcja wczytująca dane z pliku Data.txt
def load_data(filename="Data.txt"):
    records = []
    if not os.path.exists(filename):
        print(f"Plik {filename} nie istnieje!")
        return records
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            fields = line.split(";")
            if len(fields) != 7:
                print(f"Pominięto niepoprawny rekord: {line}")
                continue
            record = {
                "creator": fields[0],
                "title": fields[1],
                "duration_sec": int(fields[2]),
                "game": fields[3],
                "upload_year": int(fields[4]),
                "views": int(fields[5]),
                "thumbnail": fields[6]
            }
            records.append(record)
    return records

#Funkcja wyświetlająca wszystkie rekordy
def display_all(records):
    if not records:
        print("Brak danych do wyświetlenia.")
        return

    print("\n--- LISTA WSZYSTKICH REKORDÓW ---")
    for r in records:
        print(
            f"Creator: {r['creator']}, "
            f"Title: {r['title']}, "
            f"Duration: {r['duration_sec']} s, "
            f"Game: {r['game']}, "
            f"Year: {r['upload_year']}, "
            f"Views: {r['views']}, "
            f"Thumbnail: {r['thumbnail']}"
        )


#Funkcja główna programu
def main():
    print("-----APLIKACJA KONSOLÓWA: KLIPY-----")
    records = load_data()
    display_all(records)

#Uruchomienie programu
main()
