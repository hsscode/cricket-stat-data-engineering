from googleapiclient.discovery import build

def trigger_df_job(cloud_event, environment):   
    service = build('dataflow', 'v1b3')
    project_id = "plucky-function-430114-f3"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bqload_cricket",  # Provide a unique name for the job
        "parameters": {
            "javascriptTextTransformGcsPath": "gs://bkt-cricket/udf.js",
            "JSONPath": "gs://bkt-cricket/bq.json",
            "javascriptTextTransformFunctionName": "transform",
            "outputTable": "plucky-function-430114-f3:reports.cricket_table",
            "inputFilePattern": "gs://bkt-cricket/batsmen_rankings.csv",
            "bigQueryLoadingTemporaryDirectory": "gs://bkt-cricket/temp/",
        }
    }

    request = service.projects().templates().launch(projectId=project_id, gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
