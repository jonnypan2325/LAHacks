console.log("This is a popup!")

document.getElementById('Voice').addEventListener('click', function() {
    // Get the current active tab
    console.log("twice")
});

document.getElementById('Volume').addEventListener('click', function() {
    // Get the current active tab
    console.log("once")
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      // Check if the tabs array is not empty
      if (tabs && tabs.length > 0) {
        console.log("works??")
        // Execute transcribe.js script in the current active tab
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id }, // Use the tabId of the current active tab
          files: ['transcribe.js']
        });
      } else {
        console.error("No active tab found.");
      }
    });
  });

// Function to run a script when the toggle is checked
function runTranscript() {
    // Check if the toggle is checked
    const toggle = document.getElementById('toggle');
    if (toggle.checked) {
        console.log("Toggle is on, running transcript.js");

        // Create a new script element
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'transcript.js';  // Ensure `transcript.js` is in your project directory or has a correct path
        
        // Append the script to the document head to execute it
        document.head.appendChild(script);

    } else {
        console.log("Toggle is off, removing transcript.js");

        // Find the script element and remove it (optional, if you want to unload it when toggle is off)
        const loadedScript = document.querySelector('script[src="transcript.js"]');
        if (loadedScript) {
            document.head.removeChild(loadedScript);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Add event listener to the toggle checkbox
    const toggle = document.getElementById('toggle');
    toggle.addEventListener('change', runTranscript);
});