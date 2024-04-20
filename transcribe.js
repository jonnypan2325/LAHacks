const { SpeechClient } = require('@google-cloud/speech').v1p1beta1;
const { Transform } = require('stream');

const client = new SpeechClient();

// Define a Transform stream to convert audio stream chunks to buffers
class AudioBufferStream extends Transform {
  constructor(options) {
    super(options);
  }

  _transform(chunk, encoding, callback) {
    if (chunk) {
      this.push(chunk);
    }
    callback();
  }
}

async function transcribeStreaming(projectId, audioStream) {
  const config = {
    encoding: 'LINEAR16',
    sampleRateHertz: 44100, // Adjust according to your audio stream
    languageCode: 'en-US',
    model: 'default',
    enableAutomaticPunctuation: true
  };

  const request = {
    config,
    interimResults: false
  };

  // Create a new recognize stream
  const recognizeStream = client.streamingRecognize(request)
    .on('error', console.error)
    .on('data', data => {
      if (data.results[0] && data.results[0].alternatives[0]) {
        console.log(`Transcription: ${data.results[0].alternatives[0].transcript}`);
        // Write the transcription to a file
        // Here you can write it to a file using Node.js file system API
      }
    });

  // Convert the media stream to buffers and pipe it to the recognize stream
  audioStream.pipe(new AudioBufferStream()).pipe(recognizeStream);
}

async function main() {
    const stream = await navigator.mediaDevices.getDisplayMedia({ audio: true, video: true });
    transcribeStreaming('LingoLive', stream);
  }
  
  // Call the main function to start execution
  main().catch(console.error);