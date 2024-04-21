// Define function to continuously retrieve data
function retrieveData() {
    chrome.storage.local.get('myData', function(result) {
        var data = result.myData || {};
        console.log('Retrieved data:', data);
    });
}

// Run function continuously
setInterval(function() {
    retrieveData();
}, 1000);

// chrome.runtime.onInstalled.addListener(() => {
//     chrome.action.setBadgeText({
//       text: "OFF",
//     });
//   });

// const extensions = 'https://developer.chrome.com/docs/extensions'
// const webstore = 'https://developer.chrome.com/docs/webstore'

// chrome.action.onClicked.addListener(async (tab) => {
//   if (tab.url.startsWith(extensions) || tab.url.startsWith(webstore)) {
//     // Retrieve the action badge to check if the extension is 'ON' or 'OFF'
//     const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
//     // Next state will always be the opposite
//     const nextState = prevState === 'ON' ? 'OFF' : 'ON'

//     // Set the action badge to the next state
//     await chrome.action.setBadgeText({
//       tabId: tab.id,
//       text: nextState,
//     });
//   }
//   if (nextState === "ON") {
//     // Insert the CSS file when the user turns the extension on
//     await chrome.scripting.insertCSS({
//       files: ["focus-mode.css"],
//       target: { tabId: tab.id },
//     });
//   } else if (nextState === "OFF") {
//     // Remove the CSS file when the user turns the extension off
//     await chrome.scripting.removeCSS({
//       files: ["focus-mode.css"],
//       target: { tabId: tab.id },
//     });
//   }
// });

// document.addEventListener('DOMContentLoaded', function() {
//   var popupContent = document.getElementById('popup-content');
//   var closeButton = document.getElementById('closeButton');

//   // Show the popup
//   popupContent.style.display = 'block';

//   // Add event listener to the close button
//   // closeButton.addEventListener('click', function() {
//   //     // Hide the popup
//   //     popupContent.style.display = 'none';
//   // });

//   // Prevent the default behavior of closing the popup when clicking outside of it
//   closeButton.addEventListener('click', function(event) {
//       if (!popupContent.contains(event.target)) {
//           event.preventDefault();
//       }
//   });

//   // Prevent the default behavior of closing the popup when pressing the Escape key
//   document.addEventListener('keydown', function(event) {
//       if (event.key === 'Escape') {
//           event.preventDefault();
//       }
//   });
// });