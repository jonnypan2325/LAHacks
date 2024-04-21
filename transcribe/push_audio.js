// Import the functions you need from the SDKs you need
import firebase from 'firebase/app';
import 'firebase/storage';
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBjY45pMs-xXn_f-PfUY9USkHWmw43KWBw",
    authDomain: "lingolive.firebaseapp.com",
    projectId: "lingolive",
    storageBucket: "lingolive.appspot.com",
    messagingSenderId: "545528818041",
    appId: "1:545528818041:web:e8ab78c2d95af35890a7a8",
    measurementId: "G-GGV31J4577"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const storage = firebase.storage();

chrome.tabCapture.capture({ audio: true }, async (stream) => {
    // Continue to play the captured audio to the user.
    const output = new AudioContext();
    const source = output.createMediaStreamSource(stream);
    source.connect(output.destination);

    // Send audio stream to Firebase Storage
    const mediaRecorder = new MediaRecorder(stream);
    let chunks = [];

    mediaRecorder.ondataavailable = (e) => {
      chunks.push(e.data);
    };

    mediaRecorder.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/wav' }); // Blob with MIME type for WAV audio
      const storageRef = storage.ref();
      const timestamp = new Date().getTime(); // Get current timestamp
      const audioRef = storageRef.child(`audio_${timestamp}.wav`);


      await audioRef.put(blob); // Upload Blob to Firebase Storage
    };

    mediaRecorder.start();
    setTimeout(() => {
      mediaRecorder.stop();
    }, 5000); // Record for 5 seconds
  });
