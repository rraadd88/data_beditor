import pandas as pd
pd.set_option('display.max_colwidth', -1)
dlibrary=pd.read_table('dlibraries.tsv')
# dlibrary['dataset']=dlibrary.apply(lambda x : f"{x['dataset']} ({x['organism']})",axis=1)
# dlibrary=dlibrary.set_index('dataset')
dlibrary.to_html('dlibraries.html',index=False)
with open('dlibraries.html','r') as f:
#     insert_lines=f.readlines()[1:]
    insert=''.join(f.readlines()[1:])
with open('template.html','r') as f:
    template=''.join(f.readlines())
tbody=f"<tbody> {insert.split('<tbody>')[1]}"
thead=insert.split('<tbody>')[0].replace('text-align: right','text-align: left')
tfoot=insert.split('<tbody>')[0].replace('thead','tfoot').replace('text-align: right','text-align: left')
datatable=thead+tfoot+tbody
datatable=datatable.replace('&lt;\\','</').replace('&lt;','<').replace('&gt;','>')
with open('index.html','w') as f:
    f.write(template.replace('{datatable}',datatable))
