# googlecloud
# the scripts makes a backup of files in the google cloud. automatically creates folders acc ording to the prefix in the google bucket and saves everyting inside the folder named after the bucket. The script is capable of only downloading new files insted of whole files if the backup has already initiated.

# the code creates RsdGoogleClooudBackup object which needs path to google key file as a paramter.

# the method RsdGoogleBucketPrefix could be used to get the name of prefix in the google colud bucket and requires following parameter
# bucket = name of the google cloud bucket
# the method RsdGoogleCloudDownload could be used to download the files from the google cloud bucket and requires following parameters
# path = the destination folder where the files are to be saved
# bucket = name of the google cloud bucket
# sub_directory = 'y' or 'n' if the bucket contains prefix
# first_time_backup = 'y' or 'n'. however this could be ignored becasue the script will asks later to conform.
# y = if the backup is done for the first time , n = if backup is already done before and just need to be updated with new files instead of downloading whole files.
