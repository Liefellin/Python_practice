def fibonacci(end, spark=1, quo=0):
    for i in range(end):
        yield quo
        history = quo
        quo = spark
        spark = quo + history
