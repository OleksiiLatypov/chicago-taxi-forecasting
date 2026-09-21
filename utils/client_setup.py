# Set up Google Cloud service account keys 
def setup_gcp_creds(credentials_path: str):
    if os.path.exists(credentials_path):
        try:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= credentials_path
            logger.info(f"Found service account file")
            client = storage.Client()
            buckets = list(client.list_buckets())
            logger.info(f"Successfully authenticated. Found {len(buckets)} buckets.")
        except Exception as e:
            logger.error(f"File credential file exists but authentection failed")
            logger.error(f"Details: {e}")
    else:
        print(f"Service account file NOT FOUND at: {credentials_path}")
        dbutils.notebook.exit("File not found")
