
def max_nepali_day(request):
    from modules.getting_days import get_max_np_day
    year, month = request.GET['year'], request.GET['month']
    realMaxDate = {get_max_np_day(year, month)}
    print(realMaxDate)
    return HttpResponse(realMaxDate)



def todaydate(request):
    import nepali_datetime
    date = str(nepali_datetime.date.today()).split('-')
    date = {'year':date[0],'month':date[1], 'day':date[2]}
    return JsonResponse(date)