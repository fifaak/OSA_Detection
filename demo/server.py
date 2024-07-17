import time
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import openpyxl
import json
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def stream_data(file_path: str):
    # Open the .xlsx file
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    # Extract headers
    headers = [cell.value for cell in sheet[1]]
    
    # Stream data row by row starting from the second row (first row is headers)
    for row in sheet.iter_rows(values_only=True, min_row=2):
        row_data = {headers[i]: cell for i, cell in enumerate(row)}
        yield json.dumps(row_data) + "\n"
        time.sleep(0.5)

@app.get("/stream", response_class=StreamingResponse)
async def stream_xlsx():
    file_path = "./db/db.xlsx"  # Path to your .xlsx file
    return StreamingResponse(stream_data(file_path), media_type="application/json")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
