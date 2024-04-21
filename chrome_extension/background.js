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

