from time import perf_counter

import cv2
from ultralytics import YOLO

STREAM_URL = "http://192.168.100.8:8080/video"


def main():
    print("Loading YOLOv8n...")
    model = YOLO("yolov8n.pt")

    print("Connecting to phone camera...")
    capture = cv2.VideoCapture(STREAM_URL)

    try:
        if not capture.isOpened():
            print("Could not connect. Check the phone IP and camera server.")
            return

        print("Detection started. Click the video window and press Q to quit.")

        frame_count = 0
        report_start = perf_counter()

        while True:
            success, frame = capture.read()

            if not success:
                print("Could not read a frame. The stream may have stopped.")
                break

            result = model.predict(
                source=frame,
                imgsz=320,
                conf=0.4,
                device="cpu",
                verbose=False,
            )[0]

            annotated_frame = result.plot()
            cv2.imshow("Phone Camera - YOLOv8 Detection", annotated_frame)

            # Process window events and check for the quit key.
            key = cv2.waitKey(1) & 0xFF

            frame_count += 1
            elapsed = perf_counter() - report_start

            if elapsed >= 5.0:
                fps = frame_count / elapsed
                print(f"Receiver/detection throughput: {fps:.1f} FPS")

                frame_count = 0
                report_start = perf_counter()

            if key == ord("q"):
                break

    finally:
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()