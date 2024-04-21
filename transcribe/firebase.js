// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCf6DzzqN_O_R4quw3QHQGH5g7kHT7JtPE",
  authDomain: "lingolive-db334.firebaseapp.com",
  projectId: "lingolive-db334",
  storageBucket: "lingolive-db334.appspot.com",
  messagingSenderId: "167921300469",
  appId: "1:167921300469:web:9a79143d4676a6c29826bc",
  measurementId: "G-HP4QMJ64HF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const storage = getStorage(app);


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

    // Create a Blob when recording stops
    mediaRecorder.onstop = () => {
      const blob = new Blob(chunks, { type: 'audio/wav' }); // Blob with MIME type for WAV audio
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