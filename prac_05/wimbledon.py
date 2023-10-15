"""
CP1404/CP5632 Practical 5
read and process tenis data
Estimate: 30 minutes
Actual:   43 minutes
"""



def main():
    """Read data file and print details about Wimbledon champions and countries."""
    filename = "wimbledon.csv"
    records = get_records(filename)
    champs, countries = compile_records(records)
    display_winners(champs, countries)


def compile_records(records):
    """Generate dict for champs and list for country and record."""
    country = 1
    champ = 2
    champs = {}
    countries = set()
    for record in records:
        countries.add(record[country])
        try:
            champs[record[champ]] += 1
        except KeyError:
            champs[record[champ]] = 1
    return champs, countries


def display_winners(champs, countries):
    """show champs and counrty"""
    print("The Wimbledon Champs are: ")
    for name, count in champs.items():
        print(name, count)
    print(f"\nThe below {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """get the records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()