# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:54:59 2023

@author: ryan

"""

import pandas as pd
import streamlit as st
import json

# JSON格式转换
@st.cache_data
def convert_df(data):
    df = pd.read_excel(data)
    json_data = df.to_json(orient='records')
    # json_obj = json.loads(json_data)
    return json_data


# 页面绘制
st.title('Excel转JSON工具')
st.info('上传Excel，每一列会被处理为JSON格式')
st.write(' ')

st.header('Step 1. 上传Excel表格')
file = st.file_uploader('选择数据文件（仅.xlsx格式）')

js_data = convert_df(file)

st.header('Step 2. 下载JSON文件')
st.download_button(label='下载数据模板',
                   data=js_data,
                   file_name='output.json',
                   mime='json')