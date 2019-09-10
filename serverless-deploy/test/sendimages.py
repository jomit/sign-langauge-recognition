from azure.storage.queue import QueueService, QueueMessageFormat
import base64
queue_service = QueueService(connection_string="")
queue_service.encode_function = QueueMessageFormat.text_base64encode

for y in range(1, 4):
    for x in range(0, 100):
        queue_service.put_message('images', f"https://<STORAGE-ACCOUNT-NAME>.blob.core.windows.net/testimages/A/A0.jpg")
        queue_service.put_message('images', f"https://<STORAGE-ACCOUNT-NAME>.blob.core.windows.net/testimages/B/B0.jpg")
        queue_service.put_message('images', f"https://<STORAGE-ACCOUNT-NAME>.blob.core.windows.net/testimages/C/C0.jpg")
        queue_service.put_message('images', f"https://<STORAGE-ACCOUNT-NAME>.blob.core.windows.net/testimages/D/D0.jpg")