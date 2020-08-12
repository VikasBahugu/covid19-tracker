from django.shortcuts import render
from covid import Covid
import datetime

covid = Covid(source="worldometers")

def homepage(request):
    confirmed = covid.get_total_confirmed_cases()
    confirmedp = round(confirmed/7594300000 * 100,2)

    active = covid.get_total_active_cases()
    activep = round(active / confirmed * 100, 2)

    recovered = covid.get_total_recovered()
    recoveredp = round(recovered / confirmed * 100, 2)

    deaths = covid.get_total_deaths()
    deathsp = round(deaths / confirmed * 100, 2)


    coutry_case = []
    covids = covid.get_data()
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)
    covids.pop(0)



    now = datetime.datetime.now()

    params = {
        'timenow': now,
        'activep': activep,
        'recoveredp': recoveredp,
        'confirmedp': confirmedp,
        'deathsp': deathsp,
        'covid_data': covids,
    }
    return render(request, 'homepage.html', params)