document.addEventListener('DOMContentLoaded', function() {
    var saveToggle = document.getElementById('saveToggle');

    chrome.storage.local.get('toggleState', function(result) {
        if (result.toggleState) {
            saveToggle.checked = true;
        }
    });

    saveToggle.addEventListener('change', function() {
        chrome.storage.local.set({ 'toggleState': saveToggle.checked });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var dropdownSelect1 = document.querySelector('.column-language-select-inp select');

    dropdownSelect1.addEventListener('change', function(event) {
        var selectedValue1 = event.target.value;

        localStorage.setItem('selectedLanguage', selectedValue1);

        console.log('Selected value saved to local storage:', selectedValue1);

        // Store data
        chrome.storage.local.set({ userName: 'erika' }, () => {
            console.log('Data saved');
        });

        // Retrieve data
        chrome.storage.local.get(['userName'], (result) => {
            console.log('User name:', result.userName);
});
        
    });

    var savedValue = localStorage.getItem('selectedLanguage');

    if (savedValue) {
        dropdownSelect1.value = savedValue;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var dropdownSelectOut = document.querySelector('.column-language-select-out select');

    dropdownSelectOut.addEventListener('change', function(event) {
        var selectedValueOut = event.target.value;

        localStorage.setItem('selectedLanguageOut', selectedValueOut);

        console.log('Selected value for output saved to local storage:', selectedValueOut);
    });

    var savedValueOut = localStorage.getItem('selectedLanguageOut');

    if (savedValueOut) {
        dropdownSelectOut.value = savedValueOut;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var volumeSlider = document.getElementById('volumeSlider');

    volumeSlider.addEventListener('input', function() {
        var volume = volumeSlider.value;

        localStorage.setItem('volumeLevel', volume);

        volumeSlider.style.background = 'linear-gradient(to right, #4CAF50 0%, #4CAF50 ' + volume + '%, #d3d3d3 ' + volume + '%, #d3d3d3 100%)';

        console.log('Volume level saved to local storage:', volume);
    });

    var savedVolume = localStorage.getItem('volumeLevel');

    if (savedVolume) {
        volumeSlider.value = savedVolume;
        volumeSlider.style.background = 'linear-gradient(to right, #4CAF50 0%, #4CAF50 ' + savedVolume + '%, #d3d3d3 ' + savedVolume + '%, #d3d3d3 100%)';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var dropdownSelectOut = document.querySelector('.column-voice-select select');

    dropdownSelectOut.addEventListener('change', function(event) {
        var selectedValueOut = event.target.value;

        localStorage.setItem('selectedVoiceOut', selectedValueOut);

        console.log('Selected value for output saved to local storage:', selectedValueOut);
    });

    var savedValueOut = localStorage.getItem('selectedVoiceOut');

    if (savedValueOut) {
        dropdownSelectOut.value = savedValueOut;
    }
});