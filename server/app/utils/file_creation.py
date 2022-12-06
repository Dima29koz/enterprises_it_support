import io
import csv
import json
import yaml

from server.app.pr11.models import NewsDBItem


def get_file(objects: list, file_format: str):
    match file_format:
        case 'csv':
            return get_csv(objects)
        case 'json':
            return get_json(objects)
        case 'yaml':
            return get_yaml(objects)
        case _:
            return


def get_csv(objects):
    proxy = io.StringIO()
    writer = csv.writer(proxy)
    writer.writerow([column.name for column in NewsDBItem.__mapper__.columns])
    [writer.writerow(
        [getattr(curr, column.name) for column in NewsDBItem.__mapper__.columns]) for curr in objects]
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    proxy.close()
    return mem


def get_json(objects):
    proxy = io.StringIO()
    json.dump([obj.to_dict() for obj in objects], proxy, ensure_ascii=False)
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    proxy.close()
    return mem


def get_yaml(objects):
    proxy = io.StringIO()
    yaml.dump([obj.to_dict() for obj in objects], proxy, allow_unicode=True, encoding='utf-8')
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    proxy.close()
    return mem

