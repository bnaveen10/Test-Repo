from datetime import datetime

def main():
    now = datetime.now().isoformat()
    result = f"Workflow ran successfully at: {now}\n"

    print(result)

    with open("result.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
