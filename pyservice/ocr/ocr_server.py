import grpc
from concurrent import futures
from grpc_util.ocr_pb2 import OCRResponse
from grpc_util.ocr_pb2_grpc import OCRServiceServicer, add_OCRServiceServicer_to_server
# import pytesseract
# from PIL import Image
# import io


class OCRServiceServicer(OCRServiceServicer):
    def ExtractText(self, request, context):
        # image = Image.open(io.BytesIO(request.image))
        # text = pytesseract.image_to_string(image)
        return OCRResponse(text="i recieved")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_OCRServiceServicer_to_server(OCRServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
