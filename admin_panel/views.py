from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from customer.models import Customer
from django.utils.timezone import now
from django.http import JsonResponse

@staff_member_required
def all_requests(request):
    # Fetch all service requests for users with the appropriate permissions (support staff)
    requests = ServiceRequest.objects.all()
    return render(request, 'admin_panel/all_requests.html', {'requests': requests})

@staff_member_required
def update_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        if new_status == 'resolved':
            service_request.resolved_at = now()
        service_request.save()

        # Return updated request data as JSON
        data = {
            'id': service_request.id,
            'status': service_request.status,
            'resolved_at': service_request.resolved_at,
            'submitted_at': service_request.submitted_at.strftime('%d-%b-%Y %H:%M'),
            'customer_name': service_request.customer.name,
            'request_type': service_request.request_type,
        }
        return JsonResponse({'success': True, 'request': data})
        return redirect('all_requests')

    return render(request, 'admin_panel/update_request.html', {'service_request': service_request})
