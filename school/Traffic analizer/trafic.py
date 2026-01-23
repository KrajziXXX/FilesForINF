drive = {
    "max_s": 138,
    "avg_s": 74,
    "acceleration_e": 12,
    "harsh_braking": 5,
    "distance_km": 34,
    "speed_events": 3,
    "fuel_used": 3.2,  #dla elektryka: kWh
    "where": "miasto",
    "engine_type": "diesel",  #diesel/benzyna/gaz/hybryda/elektryk
    "engine_capacity_cc": 1900,  #dla spalinowych
    "engine_power_kw": None,     #dla elektryków
    "vehicle_weight_kg": 1500
}

def fuel_efficiency(data):
    #Obliczanie efektywności paliwowej lub zużycia energii elektrycznej
    if data["engine_type"] == "elektryk":
        efficiency = (data["fuel_used"] / data["distance_km"]) * 100
        return f"Zużycie energii: {round(efficiency, 2)} kWh/100km"
    else:
        efficiency = (data["fuel_used"] / data["distance_km"]) * 100
        return f"Spalanie: {round(efficiency, 2)} L/100km"

def driving_style(data):
    #Ocena stylu jazdy na podstawie różnych parametrów
    score = 100

    #Kara za zbyt dużą prędkość maksymalną
    if data["max_s"] > 120 and data["where"] == "miasto":
        score -= 40
    elif data["max_s"] > 140 and data["where"] == "trasa":
        score -= 25

    #Kara za zbyt wysoką średnią prędkość
    if data["avg_s"] > 80 and data["where"] == "miasto":
        score -= 25
    elif data["avg_s"] > 100 and data["where"] == "trasa":
        score -= 15

    #Kara za gwałtowne przyspieszenia, hamowania i inne zdarzenia
    score -= data["acceleration_e"] // 3
    score -= data["harsh_braking"] // 2
    score -= data["speed_events"] // 3

    #Zwrot oceny stylu jazdy na podstawie wyniku
    if score >= 70:
        return "Spokojny styl jazdy"
    elif score >= 35:
        return "Dynamiczny styl jazdy"
    else:
        return "Niebezpieczny styl jazdy"

def engine_info(data):
    #Generowanie informacji o silniku na podstawie typu pojazdu
    if data["engine_type"] in ["diesel", "benzyna", "gaz", "hybryda"]:
        print("Sprawdzanie silnika spalinowego...")
        return (f"Silnik: {data['engine_type'].capitalize()}, "
                f"Pojemność: {data['engine_capacity_cc']} cm³, "
                f"Waga pojazdu: {data['vehicle_weight_kg']} kg")
    elif data["engine_type"] == "elektryk":
        print("Sprawdzanie silnika elektrycznego...")
        if data["engine_power_kw"] is None:
            print("Brak danych o mocy silnika elektrycznego!")
        return (f"Silnik: Elektryczny, Moc: {data['engine_power_kw']} kW, "
                f"Waga pojazdu: {data['vehicle_weight_kg']} kg")
    else:
        print("Nieznany typ silnika!")
        return "Nieznany typ silnika"

def driving_recommendations(data):
    #Generowanie rekomendacji dotyczących stylu jazdy na podstawie specyfikacji pojazdu
    print("Generowanie rekomendacji dotyczących stylu jazdy...")
    if data["engine_type"] == "diesel":
        if data["engine_capacity_cc"] > 2000:
            return ("Zalecany spokojny styl jazdy, aby zmniejszyć zużycie paliwa. "
                    "Unikaj jazdy na krótkich dystansach, aby zapobiec zapychaniu filtra DPF. "
                    "Regularnie sprawdzaj jakość paliwa i stosuj dodatki czyszczące.")
        else:
            return ("Możesz jeździć dynamicznie, ale pamiętaj o ekonomii paliwowej. "
                    "Unikaj jazdy na krótkich dystansach, aby chronić filtr DPF.")
    elif data["engine_type"] == "benzyna":
        return ("Możesz jeździć dynamicznie, ale pamiętaj o regularnym serwisowaniu silnika. "
                "Stosuj paliwo wysokiej jakości, aby uniknąć osadów w układzie paliwowym.")
    elif data["engine_type"] == "gaz":
        return ("Zalecany spokojny styl jazdy, aby zoptymalizować zużycie gazu. "
                "Regularnie sprawdzaj szczelność instalacji gazowej i wymieniaj filtry.")
    elif data["engine_type"] == "hybryda":
        return ("Wykorzystuj tryb elektryczny w mieście i unikaj gwałtownych przyspieszeń. "
                "Dbaj o stan baterii i regularnie serwisuj układ hybrydowy.")
    elif data["engine_type"] == "elektryk":
        if data["vehicle_weight_kg"] > 2000:
            return ("Unikaj gwałtownych przyspieszeń, aby zwiększyć zasięg. "
                    "Planuj ładowanie baterii z wyprzedzeniem, szczególnie na dłuższe trasy.")
        else:
            return ("Możesz jeździć dynamicznie, ale pamiętaj o ładowaniu baterii. "
                    "Unikaj całkowitego rozładowania baterii, aby wydłużyć jej żywotność.")
    else:
        return "Brak wystarczających danych do wygenerowania rekomendacji."

#Wywołania funkcji i wyświetlanie wyników
print("Ocena stylu jazdy:")
print(driving_style(drive))
print("\nEfektywność paliwowa:")
print(fuel_efficiency(drive))
print("\nInformacje o silniku:")
print(engine_info(drive))
print("\nRekomendacje dotyczące stylu jazdy:")
print(driving_recommendations(drive))