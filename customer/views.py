from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Ensure the user is authenticated before accessing this view
@login_required
def customer_home(request):
    return render(request, 'customer/home.html') 
    
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            try:
                service_request.customer = request.user.customer
            except Customer.DoesNotExist:
                # Create a Customer profile if it doesn't exist
                customer = Customer.objects.create(
                    user=request.user,
                    name=request.user.username,
                    email=request.user.email
                )
                service_request.customer = customer

            service_request.save()
            # Return the newly created request data as JSON
            request_data = {
                'id': service_request.id,
                'request_type': service_request.request_type,
                'status': service_request.status,
                'submitted_at': format(service_request.submitted_at, 'Y-m-d H:i:s'),
                'resolved_at': service_request.resolved_at and format(service_request.resolved_at, 'Y-m-d H:i:s'),
            }
            return JsonResponse({'success': True, 'request': request_data})

        # Handle form errors
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    try:
        # Fetch the requests of the authenticated customer
        requests = ServiceRequest.objects.filter(customer=request.user.customer)
        return render(request, 'customer/track_requests.html', {'requests': requests})
    except Customer.DoesNotExist:
        return render(request, 'customer/error.html', {
            'message': 'No customer profile exists for this user. Please contact support.'
        })
