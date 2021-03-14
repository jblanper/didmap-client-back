import uvicorn

def main():
    uvicorn.run("didmap_api.main:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()