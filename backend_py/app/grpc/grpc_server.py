import grpc


class OCRService():
    """"""

    def exteract_text(self, request, context):
        file_bytes = request.file_bytes
