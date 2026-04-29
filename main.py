from fastapi import FastAPI, UploadFile, File, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os

app = FastAPI()

os.makedirs("uploads", exist_ok=True)

# Mount static files
app.mount("/files", StaticFiles(directory="uploads"), name="files")


@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    allowed_types = ["image/png", "image/jpeg"]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="only png and jpeg files are allowed",
        )
    content = await file.read()

    if len(content) > 1 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="file size must be under 1MB",
        )

    filepath = f"uploads/{file.filename}"
    with open(filepath, "wb") as f:
        f.write(content)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "file uploaded",
            "file_url": f"http://127.0.0.1:8000/files/{file.filename}",
        },
    )


@app.get("/")
def home():
    return {"message": "Uploading files"}


# @app.get("/files/{filename}")
# def view_file(filename: str):
#     return {"file_url": f"http://127.0.0.1:8000/files/{filename}"}
