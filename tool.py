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
    ex_file = pd.ExcelFile(data)
    sheets = ex_file.sheet_names
    ex_data = {}
    js_data_list = []
    js_data_name = []
    for sheet in sheets:
        js_data_name.append(str(sheet))
        ex_data[sheet] = ex_file.parse(sheet)
        # df = pd.read_excel(ex_data[sheet])
        json_data = ex_data[sheet].to_json(orient='records',force_ascii=False)
        js_data_list.append(json_data)

    return js_data_name,js_data_list


# 页面绘制
st.title('Excel转JSON工具')
st.info('上传Excel，每一列会被处理为JSON格式')
st.write(' ')

st.header('Step 1. 上传Excel表格')
file = st.file_uploader('选择数据文件（仅.xlsx格式）')

if file is not None:
    js_name,js_data = convert_df(file)

    st.header('Step 2. 下载JSON文件')
    for i in js_name:
        dl_name = str(i) + '.json'
        st.download_button(label=i,
                    data=js_data,
                    file_name=dl_name,
                    mime='json')
