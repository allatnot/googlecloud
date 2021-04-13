import os
import pandas as pd
from google.cloud import bigquery
class RsdGoogleBigquery:
    def __init__(self, key):
        self.key = key
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key
        self.qclient = bigquery.Client()
    def RsdCreateBigqueryTable(self,table_dataset,table, schema):
        qclient = self.qclient
        table_id = table_dataset+'.'+table
        tables = client.list_tables(table_dataset)
        lst = []
        for rsd in tables:
            kmr = rsd.project+'.'+rsd.dataset_id+'.'+rsd.table_id
            lst.append(kmr)
        if table_id not in lst:
            print('Creating the table...')
            sma = open(schema, 'r')
            sma = sma.read()
            fl = []
            sc = []
            for i in range(len(sma.split('\n'))):
                if i%2==0:
                    fl.append(sma.split('\n')[i])
                else:
                    sc.append(sma.split('\n')[i])
            sch = []
            for i,j in zip(fl,sc):
                sch.append(bigquery.SchemaField(i,j, mode = 'NULLABLE'))
            table = bigquery.Table(table_id, schema = sch)
            table = qclient.create_table(table)
            print('Creatd table {}.{}.{}'.format(table.project, table.dataset_id, table.table_id))
        else:
            print('The table is already exist!')
        return
    
    def RsdGoogleBigqueryLoad(self,table_id, schema, file):
        qclient = self.qclient
        smp = open(schema, 'r')
        smp = smp.read()
        fls = []
        scc = []
        for i in range(len(smp.split('\n'))):
            if i%2==0:
                fls.append(smp.split('\n')[i])
            else:
                scc.append(smp.split('\n')[i])
        skd = []
        for i,j in zip(fls,scc):
            skd.append(bigquery.SchemaField(i,j, mode = 'NULLABLE'))
    
        job_config = bigquery.LoadJobConfig(
                     schema = skd,skip_leading_rows = 1,write_dispositon = bigquery.WriteDisposition.WRITE_TRUNCATE, 
                              source_format = bigquery.SourceFormat.CSV,
                          )
        with open(file, 'rb') as rsk:
            job = qclient.load_table_from_file(rsk, table_id, job_config=job_config)
            print('Done uploading files to {0}'.format(table_id))  
        job.result()
        destination_table = qclient.get_table(table_id)
        print('Loaded {} rows'. format(destination_table.num_rows))
        return
        
