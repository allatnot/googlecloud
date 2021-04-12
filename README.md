# googlecloud
# the scripts makes a backup of files and uploads the files in the google cloud. it automatically creates folders according to the prefix in the google bucket and saves everyting inside the folder named after the bucket. The script is capable of only downloading and uploading only new files insted of whole files if the backup and uploading have already initiated.

# the code creates RsdGoogleClooudBackup object which needs following paramter
# path = to google account service key file path as a paramter.

# the method RsdGoogleBucketPrefix could be used to get the name of prefix in the google colud bucket and requires following parameter
# bucket = name of the google cloud bucket

# the method RsdGoogleCloudDownload could be used to download the files from the google cloud bucket and requires following parameters
# path = the destination folder where the files are to be saved
# bucket = name of the google cloud bucket
# sub_directory = 'y' or 'n' if the bucket contains prefix
# first_time_backup = 'y' or 'n'. however this could be ignored becasue the script will asks later to conform.
# y = if the backup is done for the first time , n = if backup is already done before and just need to be updated with new files instead of downloading whole files.

# the method RsdGoogleCloudUpload could be used to create a bucket if not exists and upload files and requires following parameters
# bucket_name = the name of bucket you wish to create or already exist bucket
# files = path where files are exit those to be uploaded
# location = google cloud location where the bucket exists
# prefix = the name of folder needs to be created inside the google cloud bucket
# record = the path where you want to keep the record of the uploaded files. 
# first_upload = 'y' if yes or 'n' if no. 
