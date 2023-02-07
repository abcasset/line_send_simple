from __future__ import absolute_import, division, print_function, with_statement
import requests
import pandas as pd 
import dataframe_image as dfi # pip install dataframe_image


def f_LINE_ACCESS_TOKEN(ai_1):
    if ai_1 == 'MM':  # 마이챗 
        LINE_ACCESS_TOKEN = "eUzLiBLtSl3xKX7TmLovyATt6LRqQFH1aiQDJkrwUjg"  # 마이챗 : 성공 
    elif ai_1 == 'GJ':  # 객장 
        LINE_ACCESS_TOKEN = "BxNfsuIuaEzbjqrfo3GOrIkwhW7E9UwHKypRPC8rTCw"  # 객장 :  성공
    elif ai_1 == 'JD':  # 자동공지 
        LINE_ACCESS_TOKEN = "LaXf5ZNMkeqfJTWWjNSXgjPLxa6wEyjlrgH3eO04LwC"  # 자동공지 
    elif ai_1 == 'TT':  # 테스트 김지원
        LINE_ACCESS_TOKEN = "Uql4Y2XHvAQt1HAOtPMy1s7ZDWUK4R2eGY9pKBeN52u"  # 김지원, else : 성공 


    elif ai_1 == 'A':  # 섹터 
        LINE_ACCESS_TOKEN = "NUtJ5PhQWHvxPIjJe52TeoJQOr8DFH9GQNz8F9sUQtw"  # 섹터 
    elif ai_1 == 'B':  # 섹터 
        LINE_ACCESS_TOKEN = "nWX6DQovi5L7rtgZRB7D7c8ZGJopZiSBoc3UA2m8tEN"  # 섹터 
    elif ai_1 == 'C':  # 섹터 
        LINE_ACCESS_TOKEN = "rgD9Ht32FeWO7EbGyZKC10B8rtSRUM2K58TF4XD0DCN"  # 섹터 
    elif ai_1 == 'D':  # 섹터 
        LINE_ACCESS_TOKEN = "1d7JXseNzCRPsPrte4mANdU59EqoUBQqEHQyTEiwbEI"  # 섹터 
    elif ai_1 == 'E':  # 섹터 
        LINE_ACCESS_TOKEN = "qLMmyoLPLGNe8FMGDPJW4Fi6g2AKFJZbyLzIwSe68xt"  # 섹터  신균 
    elif ai_1 == 'F':  # 섹터 
        LINE_ACCESS_TOKEN = "eYPQLoUUwaYDYmSXlEwy9DYAFKGnyAfOncClhuzXsIk"  # 섹터 
    elif ai_1 == 'G':  # 섹터 
        LINE_ACCESS_TOKEN = "Pl1PvtJagEs1VljNcbCEpahGDltq4VnWpNwiWi8Rwvx"  # 섹터 
    elif ai_1 == 'H':  # 섹터 
        LINE_ACCESS_TOKEN = "ExJ8N6vLnMvYJ1d9qZKq1dLrRK1qXok6WrlCrNwKreG"  # 섹터 


    else:
        LINE_ACCESS_TOKEN = "99999999999"  # 김지원, 이천주 두번재    
    return LINE_ACCESS_TOKEN


gdic_midas_sec_to_token = { 
    'MM' : "eUzLiBLtSl3xKX7TmLovyATt6LRqQFH1aiQDJkrwUjg",  # 마이챗 : 성공 
    'GG' : "BxNfsuIuaEzbjqrfo3GOrIkwhW7E9UwHKypRPC8rTCw",  # 객장 :  성공
    'JJ' : "LaXf5ZNMkeqfJTWWjNSXgjPLxa6wEyjlrgH3eO04LwC",  # 자동공지 
    'II' : "A6ebuFcCaTY9wuzXc1ovnSAGcVjHkW3TkWjO0oUi8tf",  # 인포스탁 
    'TT' : "Uql4Y2XHvAQt1HAOtPMy1s7ZDWUK4R2eGY9pKBeN52u",  # 김지원 
    'A' : 'NUtJ5PhQWHvxPIjJe52TeoJQOr8DFH9GQNz8F9sUQtw', 
    'B' : 'nWX6DQovi5L7rtgZRB7D7c8ZGJopZiSBoc3UA2m8tEN', 
    'C' : 'rgD9Ht32FeWO7EbGyZKC10B8rtSRUM2K58TF4XD0DCN', 
    'D' : '1d7JXseNzCRPsPrte4mANdU59EqoUBQqEHQyTEiwbEI', 
    'E' : 'qLMmyoLPLGNe8FMGDPJW4Fi6g2AKFJZbyLzIwSe68xt', 
    'F' : 'eYPQLoUUwaYDYmSXlEwy9DYAFKGnyAfOncClhuzXsIk', 
    'G' : 'Pl1PvtJagEs1VljNcbCEpahGDltq4VnWpNwiWi8Rwvx', 
    'H' : 'ExJ8N6vLnMvYJ1d9qZKq1dLrRK1qXok6WrlCrNwKreG'}



df  = pd.DataFrame( {'c1': ['Test', 'Test', 'Test', 'Test'], 'c2': [2, 20, 200, 2000], 'c3': [3, 30, 300, 3000]}, index=['r0', 'r1', 'r2', 'r3'] )

grim_file = 'C:\\aiq\\src\\pp6_line_send\\dataframe_grim.png'

# dfi.export(df, grim_file)

url = "https://notify-api.line.me/api/notify"

file = {'imageFile':open(grim_file,'rb')}
file = None

LINE_ACCESS_TOKEN =  f_LINE_ACCESS_TOKEN('TT')

text_data = ({ 'message':'도착여부 테스트 확인(이천주 발송)' })
LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
session.post(url, headers=LINE_HEADERS, files = file ,data=text_data, verify = False)

