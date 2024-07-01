import json
import boto3

def delete_delete_markers(s3_client, bucket_name, object_key):
  paginator = s3_client.get_paginator('list_object_versions')
  page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=object_key)
  versions_to_delete = []
  for page in page_iterator:
    print(page)
    for version in page.get('DeleteMarkers', []):
      # is_delete_marker = version.get('DeleteMarkers', False)
      is_delete_marker = True
      print(f'Is delete marker flag is {is_delete_marker}')
      if is_delete_marker:
        print('In Delete Marker')
        versions_to_delete.append({
          'Key': object_key,
          'VersionId': version['VersionId']
        })

  if versions_to_delete:
    s3_client.delete_objects(Bucket=bucket_name, Delete={
      'Objects': versions_to_delete
    })
    print(f"Deleted delete markers for object: {object_key} in bucket: {bucket_name}")

def lambda_handler(event, context):
  # TODO implement
  session = boto3.Session()
  s3_client = session.client('s3')

  # Replace with your bucket name and URL file path
  bucket_name = "testingdeletemarkergold"
  object_key = "delete_marker.py"
  delete_delete_markers(s3_client, bucket_name, object_key)
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }

