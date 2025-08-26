class ObjectDetectionModel:
    def process(self, image_data: bytes):
        """Run inference on the image (bytes). Must be implemented by subclasses."""
        raise NotImplementedError
