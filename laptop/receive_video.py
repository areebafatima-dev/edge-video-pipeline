import cv2

STREAM_URL = "http://192.168.100.8:8080/video"


def main():
    print("Connecting to phone camera...")
    capture = cv2.VideoCapture(STREAM_URL)

    try:
        if not capture.isOpened():
            print("Could not connect. Check the phone IP and camera server.")
            return

        print("Connected! Click the video window and press Q to quit.")

        while True:
            success, frame = capture.read()

            if not success:
                print("Could not read a frame. The stream may have stopped.")
                break

            cv2.imshow("Phone Camera - Laptop Receiver", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()