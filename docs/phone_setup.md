# Phone Setup — Device A

## Hardware and software
- Phone: Android smartphone
- Phone model: Not recorded
- Camera application: IP Webcam

## Video settings
- Current received stream resolution: 640 × 480 pixels
- Previous received stream resolution: 1920 × 1080 pixels
- Verification: Dimensions of decoded frames received by OpenCV
- The output resolution was changed in the phone's IP Webcam settings.
- This uses the existing app; no custom Android resizing code was written.

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
- Laptop receiver/detection throughput measured at 29.6–31.7 FPS after the first reporting interval.
- End-to-end latency has not yet been measured.
- See performance.md for the test configuration and results.

## Implementation notes
- The phone uses the existing IP Webcam application.
- No custom Android application has been developed.
- Custom phone-side resizing or compression has not been implemented.
- The laptop runs the Python receiver and neural-network detection code.