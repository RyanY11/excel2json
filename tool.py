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
        
        ex_col_data = {}
        for column in ex_data[sheet].columns:
            ex_col_data[column] = ex_data[sheet][column].tolist()
        json_data = json.dumps(ex_col_data, indent=4)
        # js_data = ex_data[sheet].to_json(orient='records',force_ascii=False)
        js_data_list.append(json_data)

    return js_data_name,js_data_list


# 页面绘制
st.title('Excel转JSON工具')
st.info('上传Excel，每一列会被处理为以列名为键，列内容列表为值的JSON格式文件')
st.write(' ')
st.text('注意！需要保证每个分表中，列名只有一行，多行列名会将非第一行内容认为是列值的一部分展示到列表中')
st.write(' ')

st.header('Step 1. 上传Excel表格')
file = st.file_uploader('选择数据文件（仅.xlsx格式）')

if file is not None:
    js_name,js_data = convert_df(file)

    st.header('Step 2. 下载JSON文件')
    for i in range(len(js_name)):
        dl_name = str(js_name[i]) + '.json'
        st.download_button(label=js_name[i],
                    data=js_data[i],
                    file_name=dl_name,
                    mime='json')

    st.text('完成~')
    st.balloon
