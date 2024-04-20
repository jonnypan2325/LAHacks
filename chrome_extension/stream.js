const stream = await navigator.mediaDevices.getDisplayMedia({ audio: true, video: true });

chrome.tabCapture.capture({ audio: true }, (stream) => {
    // Continue to play the captured audio to the user.
    const output = new AudioContext();
    const source = output.createMediaStreamSource(stream);
    source.connect(output.destination);
  
    // TODO: Do something with the stream (e.g record it)
  });