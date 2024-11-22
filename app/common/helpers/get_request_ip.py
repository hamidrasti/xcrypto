def get_request_ip(request):
    ip = (
        request.META.get("HTTP_X_FORWARDED_FOR")
        or request.META.get("HTTP_X_REAL_IP")
        or request.META.get("REMOTE_ADDR")
    )
    if ip:
        return ip.split(",")[0]
