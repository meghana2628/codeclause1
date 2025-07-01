class ObjectDetector:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    def load_model(self, model_path):
        # Load the pre-trained model for object detection
        model = cv2.dnn.readNetFromTensorflow(model_path)
        return model

    def detect_objects(self, image):
        # Prepare the image for object detection
        blob = cv2.dnn.blobFromImage(image, 1/255.0, (300, 300), (0, 0, 0), swapRB=True, crop=False)
        self.model.setInput(blob)
        detections = self.model.forward()

        objects = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Confidence threshold
                box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
                (startX, startY, endX, endY) = box.astype("int")
                objects.append((startX, startY, endX, endY, confidence))

        return objects