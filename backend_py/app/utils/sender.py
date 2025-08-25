import grpc
from pathlib import Path

from ..grpc.ocr_pb2_grpc import OCRServiceStub
from ..grpc.ocr_pb2 import OCRRequest


# HACK: this is more of a place holder code
def send_to_ocr_service(file_path):
    """
    This function send file bytes over grpc channel to ocr sernive, and returns extracted text.
    """
    ext = Path(file_path).suffix.lower()
    file_type = "pdf" if ext == ".pdf" else "image"

    with open(file_path, "rb") as f:
        file_bytes = f.read()

    channel = grpc.insecure_channel("localhost:50051")
    stub = OCRServiceStub(channel)

    request = OCRRequest(file_bytes=file_bytes, file_type=file_type)

    response = stub.ExtractText(request)

    return response.text


def get_upload_dir(levels_up: int = 2, folder_name: str = "uploads") -> Path:
    """
    Finds or creates an upload directory a given number of parent levels up.

    Args:
        levels_up (int): How many directories up from the current file's location.
        folder_name (str): The name of the uploads folder.

    Returns:
        Path: Absolute path to the uploads directory.
    """
    # Get the current file's directory
    base_dir = Path(__file__).resolve().parent

    # Go up 'levels_up' directories
    target_dir = base_dir
    for _ in range(levels_up):
        target_dir = target_dir.parent

    # Add the uploads folder path
    upload_dir = target_dir / folder_name

    # Create if it doesn't exist
    upload_dir.mkdir(parents=True, exist_ok=True)

    return upload_dir
