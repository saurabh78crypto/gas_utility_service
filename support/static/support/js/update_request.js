// Handle form submission and show the success modal
document.getElementById('updateRequestForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent actual form submission

    var form = new FormData(this); // Gather form data

    // Perform AJAX request
    fetch(updateRequestUrl, {
        method: 'POST',
        body: form,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Close the modal and show success
            var successModal = new bootstrap.Modal(document.getElementById('successModal'));
            successModal.show();

            // Automatically hide the modal after 3 seconds
            setTimeout(function () {
                successModal.hide();
                // Use the data from response to update the request in the table
                updateRequestInList(data.request);
                window.location.href = listRequestsUrl;
            }, 3000); // 3 seconds delay
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function updateRequestInList(request) {
    // Find the row corresponding to the updated request by ID
    const rows = document.querySelectorAll('#requestsTable tbody tr');
    rows.forEach(row => {
        const rowId = row.dataset.id;
        if (rowId === request.id.toString()) {
            row.querySelector('.status').textContent = request.status;
            row.querySelector('.status').className = `status-${request.status.toLowerCase()}`;
            row.querySelector('.resolved-at').textContent = request.resolved_at || 'N/A';
        }
    });
}