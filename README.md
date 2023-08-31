# excel2json

## 说明
使用pandas搭建的一个小工具，可以将Excel文件转换为JSON格式的文件，并部署到了streamlit上。

JSON文件的格式为：{"列名"：“列表形式的列值”}

## 注意事项
1. Excel表中支持多个sheet，每个sheet都将生成一个JSON文件
2. 每个sheet建议只放一行列名
3. 如果列值本身就是列表形式，此工具将保留列表形式，而不是将列表形式试做一整个字符串

## 体验路径
https://excel2json-columnshape.streamlit.app/
