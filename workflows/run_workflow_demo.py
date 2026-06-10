from workflows.engine import run_workflow

if __name__ == "__main__":
    request = "A customer wants a refund for a broken product."
    result = run_workflow(request)
    print(result)
