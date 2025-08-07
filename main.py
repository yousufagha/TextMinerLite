from etlpipeline import ETLPipeline


if __name__ == "__main__":
    url = "https://amanxai.com/2023/08/14/web-data-etl-pipeline-using-python/"
    pipeline = ETLPipeline(url)
    result_df = pipeline.run()
    result_df.to_csv("data/word_frequencies.csv", index=False)
    print(result_df.head())
