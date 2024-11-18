from django.shortcuts import render, redirect
from customer.models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def list_requests(request):
    print(f"Requested Customer: {request.user}")
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'support/list_requests.html', {'requests': requests})

