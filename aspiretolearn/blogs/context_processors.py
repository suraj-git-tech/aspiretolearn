# context_processors.py
def message_processor(request):
    if request.user.is_authenticated:
        msg = request.user.username
    else:
        msg = None
    return {
        'msg' : msg
    }