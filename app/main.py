from fastapi import FastAPI
import csv
import datetime

app = FastAPI()


def get_dict_from_csv_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def filter_sources_by_date(source_list):
    filtered_sources = []
    current_date = datetime.datetime.now()
    time_difference = datetime.timedelta(days=60)
    for item in source_list:
        if item.get('last_message_at') != '':
            last_message_date = datetime.datetime.utcfromtimestamp(int(item.get('last_message_at'))).strftime('%Y-%m-%d')
            if last_message_date == (current_date - time_difference).strftime('%Y-%m-%d'):
                filtered_sources.append(item)
    return filtered_sources


@app.get("/")
async def home():
    return filter_sources_by_date(get_dict_from_csv_file('app/sources_list.csv'))

