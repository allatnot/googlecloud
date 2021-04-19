# 1. rsdgooglecloudbackup
1.1. the script makes a backup of files and uploads the files in the google cloud. it automatically creates folders according to the prefix in the google bucket and saves     everyting inside the folder named after the bucket. The script is capable of only downloading and uploading new files insted of whole files if the backup and uploading have already initiated.
#### the code creates RsdGoogleClooudBackup object, which needs following paramter
#### key = full ptah to google account service key file.

#### the method RsdGoogleBucketPrefix could be used to get the name of prefix in the google colud bucket and requires following parameter.
#### bucket = name of the google cloud bucket

#### the method RsdGoogleCloudDownload could be used to download the files from the google cloud bucket and requires following parameters
#### path = the destination folder where the files are to be saved
#### bucket = name of the google cloud bucket
#### sub_directory = 'y' or 'n' if the bucket contains prefix
#### first_time_backup = 'y' or 'n'. however this could be ignored becasue the script will asks later to conform.
#### y = if the backup is done for the first time , n = if the backup is already done before and just need to be updated with new files instead of downloading whole files.

#### the method RsdGoogleCloudUpload could be used to create a bucket if not exists and upload files and requires following parameters
#### bucket_name = the name of bucket you wish to create or already existed bucket
#### files = full path where files exist those to be uploaded
#### location = google cloud location where the bucket should exists or ignore if bcuket is already exists.
#### prefix = the name of folder needs to be created inside the google cloud bucket
#### record = the path where you want to keep the record of the uploaded files. 
#### first_upload = 'y' if yes or 'n' if no.  If 'y' is provided the code uploads all the files in the directory if 'n' is provided the code uploads only new files in the direcotry. 'n' only should provided if the upload already done from the directory.                                                                                                                                       
# 2. rsdgooglecloudbigquery
2.1 the script creates the google bigquery table based on the schema provided externally as text (.txt) file and uploads the data in it.
#### the class RsdGoogleBigquery creates a RsdGoogleBigquery object which needs following parameter
#### key = full the path of google cloud service account key file.

#### the method RsdCreateBigqueryTable creates the bigquery table with provided schema, which needs following parameters.
#### table_dataset = project id followed by dataset.
#### table = name of the table to be created or already existed.
#### schema = full path of text file that contains schema.

#### the method RsdGoogleBigqueryLoad uploads the table in the google bigquery table and needs following parameters.
#### table_id = project id followed by dataset and table name
#### schema = text file that contains the schema
#### file = path to the csv file that needs to be uploaded
#### dispositon = one out of WRITE_TRNCATE, WRITE_APPEND, WRITE_EMPTY, the default parameter is WRITE_TRUNCATE
