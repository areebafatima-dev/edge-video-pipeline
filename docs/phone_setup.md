# Phone Setup — Device A

## Hardware and software
- Phone: Android smartphone
- Phone model: Not recorded
- Camera application: IP Webcam

## Video settings
- Received stream resolution: 1920 × 1080 pixels
- Verification: Dimensions of a decoded frame received by OpenCV

## Network addresses
- Server address: http://192.168.100.8:8080
- Video stream: http://192.168.100.8:8080/video

## Starting the system
1. Connect the phone and laptop to the same Wi-Fi.
2. Open IP Webcam on the phone.
3. Tap Start server.
4. Check the address displayed on the phone.
5. Run laptop/detect_video.py on the laptop.

## Current test results
- Live video successfully displayed in the laptop browser.
- Python successfully received and displayed the stream.
- YOLOv8 successfully detected objects in the stream.
- Detection appeared responsive during a manual test.
- FPS and end-to-end latency have not yet been measured.

## Implementation notes
- The phone uses the existing IP Webcam application.
- No custom Android application has been developed.
- Custom phone-side resizing or compression has not been implemented.
- The laptop runs the Python receiver and neural-network detection code.