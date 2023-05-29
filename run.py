import uvicorn

if __name__ == "__main__":
    uvicorn.run("fast:app",host="192.168.2.8", port=8000, log_level="info")
