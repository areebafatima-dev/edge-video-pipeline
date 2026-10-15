# Edge Video Pipeline

A two-device video-processing project using an Android phone and a Windows laptop.

The phone captures video and streams it over local Wi-Fi using IP Webcam. The laptop receives the stream, runs YOLOv8 object detection, and displays the video with detection boxes and labels.

The aim is to demonstrate a working pipeline using equipment I already have, without purchasing additional hardware.

## How it works

```text
Android phone — Device A
Camera capture and app-configured output resolution
                    |
             Local Wi-Fi stream
                    |
                    v
Windows laptop — Device B
OpenCV video reception → YOLOv8 detection → Annotated display
```

The phone's output resolution is configured in IP Webcam. I verified that changing the phone setting changed the frame dimensions received by the laptop from 1920 × 1080 to 640 × 480.

The phone uses an existing application. I have not developed a custom Android app or a custom phone-side resizing algorithm.

## Current features

- Live video streaming from an Android phone to a laptop.
- Phone-side output-resolution configuration through IP Webcam.
- Video reception and display using Python and OpenCV.
- Object detection using the pretrained YOLOv8n model.
- Detection boxes, class labels, and confidence scores.
- Receiver/detection throughput reporting approximately every five seconds.
- CPU-based inference.

## Equipment and software

### Device A — Phone

- Android smartphone.
- IP Webcam application.
- Current verified stream resolution: 640 × 480 pixels.

### Device B — Laptop

- Windows, 64-bit.
- Intel Core i7-9850H processor.
- 16 GB RAM.
- Python 3.12.
- OpenCV.
- Ultralytics YOLO.

The current implementation runs inference on the CPU. It does not use the laptop's NVIDIA GPU.

## Repository structure

```text
edge-video-pipeline/
├── docs/
│   ├── phone_setup.md
│   └── performance.md
├── laptop/
│   ├── receive_video.py
│   ├── detect_video.py
│   └── requirements.txt
├── phone/
├── .gitignore
└── README.md
```

- `receive_video.py`: Tests video reception without running detection.
- `detect_video.py`: Runs object detection and reports processing throughput.
- `phone_setup.md`: Records the phone configuration and connection procedure.
- `performance.md`: Records the initial performance test and its limitations.
- `phone/`: Reserved for future phone-side implementation files. No custom Android application is included.

## Setup

### 1. Prepare the phone

1. Install IP Webcam on the Android phone.
2. Connect the phone and laptop to the same Wi-Fi network.
3. In IP Webcam, open **Video preferences → Video resolution**.
4. Select 640 × 480, if supported.
5. Start the camera server.
6. Note the address displayed by the app.

The address used during development was:

```text
http://192.168.100.8:8080
```

The video endpoint was:

```text
http://192.168.100.8:8080/video
```

Your phone may receive a different address. Use the address currently displayed by the app.

### 2. Prepare Python

Open a PowerShell terminal in the repository's root folder.

Create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

Upgrade pip:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\laptop\requirements.txt
```

These commands use the virtual environment directly, so activation is not required.

### 3. Configure the stream address

Update `STREAM_URL` in both Python scripts to match your phone's current video endpoint:

```python
STREAM_URL = "http://192.168.100.8:8080/video"
```

Keep the camera server running while using either script.

## Running the project

### Test video reception

```powershell
.\.venv\Scripts\python.exe .\laptop\receive_video.py
```

### Run object detection

```powershell
.\.venv\Scripts\python.exe .\laptop\detect_video.py
```

On the first detection run, the application downloads `yolov8n.pt`, so internet access is needed.

Click the video window and press `Q` to stop.

## Detection configuration

The current detector uses:

```python
model.predict(
    source=frame,
    imgsz=320,
    conf=0.4,
    device="cpu",
    verbose=False,
)
```

The received stream resolution is 640 × 480. The separate `imgsz=320` setting controls model input preprocessing on the laptop; it is not the phone's transmitted resolution.

## Initial performance results

The application reports receiver/detection throughput over approximately five-second intervals.

| Measurement | Observed result |
|---|---|
| Received stream resolution | 640 × 480 |
| Model | YOLOv8n |
| Inference device | CPU |
| Inference image-size setting | 320 |
| First reporting interval | 22.4 FPS |
| Subsequent observed range | 29.6–31.7 FPS |
| Manual responsiveness check | Video appeared responsive |

These values measure the laptop processing loop, including frame reception, detection, annotation, and display-loop work.

They do not measure:

- The phone's camera capture frame rate.
- The number of unique source frames.
- End-to-end camera-to-screen latency.
- Detection accuracy against labelled test data.

See `docs/performance.md` for the recorded results.

## Implementation scope

This project combines existing tools with a Python integration:

- IP Webcam handles phone-side video capture, output configuration, and streaming.
- OpenCV handles video reception and display.
- A pretrained Ultralytics YOLOv8n model performs object detection.
- The project scripts connect these components and report processing throughput.

No model was trained from scratch, and no custom Android application has been developed.

## Current limitations

- The phone and laptop must be able to communicate over the local network.
- The stream address is configured manually.
- Automatic reconnection is not implemented.
- Camera-to-screen latency has not been measured.
- Detection accuracy has not been formally evaluated.
- The phone-side implementation depends on a third-party app.
- The current test demonstrates app-configured output resolution, not a custom preprocessing algorithm.

## Planned improvements

- Add automatic stream reconnection.
- Move the stream address into a configuration file or command-line argument.
- Measure end-to-end latency.
- Compare performance across different stream resolutions.
- Add a demonstration video.
- Explore custom phone-side preprocessing.

## Acknowledgements

This project uses IP Webcam, OpenCV, Ultralytics YOLO, and pretrained YOLOv8n weights. These are third-party components, not original implementations created for this project.