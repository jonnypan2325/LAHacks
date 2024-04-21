import './sw-omnibox.js';
import './sw-tips.js';

console.log("sw-omnibox.js")
console.log("sw-tips.js")

chrome.runtime.onInstalled.addListener(({ reason }) => {
  if (reason === 'install') {
    chrome.storage.local.set({
      apiSuggestions: ['tabs', 'storage', 'scripting']
    });
  }
});