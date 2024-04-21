document.addEventListener('DOMContentLoaded', function() {
    var popupContent = document.getElementById('popup-content');
    var closeButton = document.getElementById('closeButton');

    // Show the popup
    popupContent.style.display = 'block';

    // Add event listener to the close button
    closeButton.addEventListener('click', function() {
        // Hide the popup
        popupContent.style.display = 'none';
    });

    // Prevent the default behavior of closing the popup when clicking outside of it
    document.addEventListener('click', function(event) {
        if (!popupContent.contains(event.target)) {
            event.preventDefault();
        }
    });

    // Prevent the default behavior of closing the popup when pressing the Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            event.preventDefault();
        }
    });
});

function monitorCheckbox() {
    var checkbox = document.getElementById('toggle');
    
    // Check the state of the checkbox
    if (checkbox.checked) {
        console.log('Checkbox is checked');
        // Perform actions when the checkbox is checked
    } else {
        console.log('Checkbox is not checked');
        // Perform actions when the checkbox is not checked
    }
}

// Run the function every 1000 milliseconds (1 second)
setInterval(monitorCheckbox, 1000);