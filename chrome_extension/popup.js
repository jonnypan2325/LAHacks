console.log("This is a popup!")

document.getElementById('min30').addEventListener('click', function() {
    // Get the current active tab
    console.log("twice")
});

document.getElementById('min15').addEventListener('click', function() {
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