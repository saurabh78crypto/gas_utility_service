// Function to capitalize the first letter of each word
function capitalizeFirstLetter(str) {
    return str.replace(/\b\w/g, function(char) {
        return char.toUpperCase();
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Capitalize Request Types and Status
    const requestTypeCells = document.querySelectorAll('td');
    requestTypeCells.forEach(function(cell) {
        if (cell.closest('tr').children[0] === cell) {  // Request type column
            cell.textContent = capitalizeFirstLetter(cell.textContent);
        }
        if (cell.closest('tr').children[1] === cell) {  // Status column
            cell.textContent = capitalizeFirstLetter(cell.textContent);
        }
    });
    adjustStatusText();
});