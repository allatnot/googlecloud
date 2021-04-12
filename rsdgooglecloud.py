from google.cloud import storage
import os
import sys
from google.cloud.storage import Bucket
class RsdGoogleColudBackup:
    # create rsdGoogleCloudBackup object with google account key
    def __init__(self,key):
        '''
           key = give the path where google cloud account key exists
        '''
        self.key = key
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key
        self.client = storage.Client()
   
    # method to obtain bucket prefix  
    def RsdGetGoogleBucketPrefix(self, bucket):
        '''
            provide the bucket name
        '''
        client = self.client
        bk = client.get_bucket(bucket)
        blb = bk.list_blobs()
        rm = []
        rd = []
        for i in blb:
            rm.append(i.name)
        for i in rm:
            ms = i.split('/')
            rd.append(ms[0])
        uns = set(rd)
        prefix = list(uns)
        return prefix
    # method to download files from teh google cloud bucket  
    def RsdGoogleCloudDownload(self,path,bucket,sub_directory='n',first_time_backup = 'y'):
        '''
        path = path where you want to save downloaded files.
        bucket = name of the google bucket form where you want to get files.
        first_time_backup = y or n (case insensitive). Provide 'y' if the backup is done
                            for the first time else 'n'. However it could be ignored
                            bacause later it will be asked for the confirmation.
        sub_directory = y or n (case insensitive). Provide 'y' if the bucket has a subdirectory
                        or 'n' if the bucket has no subdirectory.
        '''
        client = self.client
        frst = first_time_backup.upper()
        while frst == 'Y' or frst == 'N':
            ins = input("Is this your first backup? Please enter 'y' for yes or 'n' for no and hit Enter : ")
            ins = ins.upper()
            const = input("Do you want to proceed? Please enter 'y' for yes or 'n' for no or 'q' for quit and hit Enter : ")
            const = const.upper()
            if (ins == 'Y' or ins == 'N') and const == 'Y':
                break
            elif const == "Q":
                sys.exit()
            else:
                print("The value is invalid. Please try again!\n")
        print('Backing up data is being carried out...')
        sub_d = sub_directory.upper()
        path = path+'/{}'.format(bucket)
        if not os.path.exists(path):
            os.mkdir(path)
            print("The directory {} created!".format(path))
        
        if sub_d == 'Y':
            bbc = client.get_bucket(bucket)
            ball = bbc.list_blobs()
            rs = []
            rr = []
            for i in ball:
                rs.append(i.name)
            for i in rs:
                rrr = i.split('/')
                rr.append(rrr[0])
            pr = set(rr)
            pref = list(pr)
            for i in pref:
                if not os.path.exists(path+'/'+i):
                    os.mkdir(path+'/'+i)
                    print('Dir {} has been created!'.format(i))
            if ins == 'Y':
                prk = path+'/processed_{}'.format(bucket)
                if not os.path.exists(prk):
                    os.mkdir(prk)
                print('Dir {} created!'.format(prk))
                with open('{}/processed_files.txt'.format(prk), 'wt') as f:
                    f.close()
            else:
                prk = path+'/processed_{}'.format(bucket)
            try:
                bkf = open('{}/processed_files.txt'.format(prk), 'r')
                bkst = bkf.read()
                bkst = bkst.split('\n')
                bkst = bkst[:-1]
                bkf.close()
            except FileNotFoundError:
                print('{} not found. May be this is your first backup! Please proceed with first backup = y'.format(prk+'/processed_files.txt'))
            print('Files are downloading...')        
            for i in range(len(rs)):
                if rs[i] not in bkst:
                    im = [j.split('/')[0] for j in rs]
                    for kd in range(len(pref)):
                        if im[i]==pref[kd]:
                            dirst = pref[kd]
                    bls = bbc.blob(rs[i])
                    bls.download_to_filename(path+'/{}/{}'.format(dirst, rs[i].replace('/', '_'))) 
                else:
                    print('File {} already downloaded!'.format(rs[i]))
            new_entry = [ie for ie in rs if ie not in bkst]
            with open('{}/processed_files.txt'.format(prk), 'a') as jh:
                for ipp in new_entry:
                    jh.write('{}\n'.format(ipp))
                jh.close()
        
        else:
            bbc = client.get_bucket(bucket)
            ball = bbc.list_blobs()
            rs = []
            for i in ball:
                rs.append(i.name)
            
            if ins == 'Y':
                prk = path+'/processed_{}'.format(bucket)
                if not os.path.exists(prk):
                    os.mkdir(prk)
                print('Dir {} created!'.format(prk))
                with open('{}/processed_files.txt'.format(prk), 'wt') as f:
                    f.close()
            else:
                prk = path+'/processed_{}'.format(bucket)
            try:
                bkf = open('{}/processed_files.txt'.format(prk), 'r')
                bkst = bkf.read()
                bkst = bkst.split('\n')
                bkst = bkst[:-1]
                bkf.close()
            except FileNotFoundError:
                print('{} not found. May be this is your first backup! Please proceed with first backup = y'.format(prk+'/processed_files.txt'))
            
            print('Files are downloding...')
            for i in range(len(rs)):
                if rs[i] not in bkst:
                    #rsd= i.name
                    bls = bbc.blob(rs[i])
                    bls.download_to_filename(path+'/{}'.format(rs[i].replace('/', '_')))
                    
                else:
                    print('File {} already downloaded!'.format(rs[i]))
            new_entry = [ie for ie in rs if ie not in bkst]
            with open('{}/processed_files.txt'.format(prk), 'a') as jh:
                for ipp in new_entry:
                    jh.write('{}\n'.format(ipp))
                jh.close()
        
        print('The data backing up has been successfully completed! You can find the files inside the folders in {}'.format(path))
        return
    def RsdGoogleCloudUpload(self,bucket_name, files, location, prefix):
        client = self.client
        bks = []
        for bucket in client.list_buckets():
            bks.append(bucket)
        bkd = [str(i).split(':')[1][1:-1] for i in bks]
        if bucket_name not in bkd:
            bucs = Bucket(client, name = bucket_name)
            bucs.create(location = location)
            co = "Y"
        else:
            co = input("The bucket is already exist. Do you want to  proceed? Enter 'y' for yes or 'n' for no and hit enter: ")
            co = co.upper()
        if co == "Y":
            print('Processing...')
        else:
            sys.exit
            
        print('Files are uploading...')
        bks = client.get_bucket(bucket_name)
        for i in os.listdir(files):
            bss = files+'/'+i
            bls = bks.blob(bss)
            bls.upload_from_filename(bss)
            bks.rename_blob(bls, '{}/{}'.format(prefix, i))
        return    
