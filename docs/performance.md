# Initial Performance Test

## Configuration
- Device A: Android phone running IP Webcam
- Received stream resolution: 640 × 480 pixels
- Connection: Local Wi-Fi
- Device B: Windows laptop
- Processor: Intel Core i7-9850H
- RAM: 16 GB
- Model: YOLOv8n, pretrained
- Inference device: CPU
- Inference image-size setting: 320
- Confidence threshold: 0.4

## Measurement method
The Python receiver counts processed frames and reports throughput
over approximately five-second intervals.

Timing covers the receiver/detection loop, including frame reception,
neural-network prediction, annotation, and display-loop work.

## Results
- First reporting interval: 22.4 FPS
- Subsequent reporting intervals:
  31.5, 31.7, 31.7, 31.7, 31.1, 30.0, 30.0, 29.9, 29.6, 30.2 FPS
- Observed range after the first interval: 29.6–31.7 FPS
- Video appeared responsive during manual observation.

## Limitations
- These values measure laptop processing throughput.
- They do not establish the phone's capture frame rate.
- Unique source frames were not independently verified.
- End-to-end camera-to-screen latency was not measured.
- Detection accuracy was not evaluated against labelled test data.