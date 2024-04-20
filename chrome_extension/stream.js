const stream = await navigator.mediaDevices.getDisplayMedia({ audio: true, video: true });

chrome.tabCapture.capture({ audio: true }, (stream) => {
    // Continue to play the captured audio to the user.
    const output = new AudioContext();
    const source = output.createMediaStreamSource(stream);
    source.connect(output.destination);
  
    // Send audio stream to server for processing
    const mediaRecorder = new MediaRecorder(stream);
    let chunks = [];

    mediaRecorder.ondataavailable = (e) => {
      chunks.push(e.data);
    };
 
    mediaRecorder.onstop = async () => {
      const blob = new Blob(chunks, { type: "audio/wav" });
      const formData = new FormData();
      formData.append("audio", blob);

    // Send to server
      await fetch("https://your-server-url.com/transcribe", {
        method: "POST",
        body: formData,
      });
    };
 
    mediaRecorder.start();
    setTimeout(() => {
      mediaRecorder.stop();
    }, 5000); // Record for 5 seconds
  });