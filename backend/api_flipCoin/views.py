from django.http import JsonResponse, HttpResponse
from tossengine.toss_engine import TossEngine2
from sqlrepos.sqlite3connection import SQLite3Connectioin
from sqlrepos.toss_engine_repo import TossEngineRepo
from datetime import datetime, date


def calculate_v2(request, *args, **kwargs):
    start_date = request.GET.get("startDate","")
    toss_number = int(request.GET.get("tossNumber",""))
    index_name = request.GET.get("indexName","")

    conn = SQLite3Connectioin().create_connection()
    with conn:
        toss_repo = TossEngineRepo(conn)
        his_id = toss_repo.add_history((datetime.now(), toss_number, index_name, datetime.strptime(start_date, '%Y-%m-%d')))
        toss_eng = TossEngine2()
        result = toss_eng.run_engine(start_date, toss_number, index_name)
        history_entries = toss_repo.prepare_history_entries(his_id, result)
        toss_repo.add_history_entries(history_entries)
        return HttpResponse(toss_eng.to_json(result), headers={"content-type":"application/json"})

def get_history_list(request, *args, **kwargs):
    conn = SQLite3Connectioin().create_connection()
    with conn:
        toss_repo = TossEngineRepo(conn)
        return JsonResponse(toss_repo.get_history_list(), safe=False)

def get_history_items(request, *args, **kwargs):
    history_id = int(request.GET.get("historyId",""))
    conn = SQLite3Connectioin().create_connection()
    with conn:
        toss_repo = TossEngineRepo(conn)
        return JsonResponse(toss_repo.get_history_items(history_id), safe=False)