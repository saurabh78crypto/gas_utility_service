function handleFormSubmission(event) {
    event.preventDefault(); 

    const form = document.getElementById('serviceRequestForm');
    const submitButton = form.querySelector('button[type="submit"]');

    // Disable the submit button to prevent multiple submissions
    submitButton.disabled = true;
    submitButton.innerText = "Submitting...";

    const formData = new FormData(form); 

    axios.post(submitRequestUrl, formData, {
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // CSRF protection
            'Content-Type': 'multipart/form-data'
        }
    }).then(response => {
        // Show success modal
        let successModal = new bootstrap.Modal(document.getElementById('successModal'));
        successModal.show();

        form.reset();

        // Update Track Requests table without refreshing
        if (response.data.success) {
            const request = response.data.request;
            const trackTable = document.querySelector('#track-requests-table tbody');

            const newRow = `
                <tr>
                    <td>${request.request_type}</td>
                    <td class="status-${request.status.toLowerCase()}">${request.status}</td>
                    <td>${request.submitted_at}</td>
                    <td>${request.resolved_at || 'N/A'}</td>
                </tr>
            `;
            trackTable.innerHTML += newRow;
        }
        // Re-enable the submit button
        submitButton.disabled = false;
        submitButton.innerText = "Submit Request";
    }).catch(error => {
        console.error("Error submitting request:", error);
        // Re-enable the submit button
        submitButton.disabled = false;
        submitButton.innerText = "Submit Request";
    });
}