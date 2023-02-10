import requests # pip3 install requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2021-10-21&endtime=2021-11-22"
resp = requests.get(url)
resp.raise_for_status()

quake_dicts = []
for row in resp.json()["features"]:
    quake_dicts.append({
        "place": row["properties"]["place"],
        "time": row["properties"]["time"],
        "mag": row["properties"]["mag"],
        "loc": {"lat": row["geometry"]["coordinates"][1],
                "lon": row["geometry"]["coordinates"][0]}
    })
print(quake_dicts)
