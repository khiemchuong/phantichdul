import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Đọc dữ liệu từ file 
ch=pd.read_csv("D:\ds_salaries (1).csv")
#Tạo danh sách 
doanh_thu=['thấp','trung bình','khá','cao']
dieu_kien=[50000,100000,150000,200000,2500000]
ch['lương']=pd.cut(ch['salary'],bins=dieu_kien,labels=doanh_thu)
doanh_thu="thấp","trung bình","khá","cao"
tan_so=ch['lương'].value_counts()
print(ch)
# tạo bản thông kê
dieu_kien1=['M','L','S']
quy_mo='company_size'
tan_so1=ch[quy_mo].value_counts()
print(ch)
#lọc dữ liệu
chuong=ch.loc[ch['job_title']=='Data Scientist']
chuong1=ch.loc[ch['job_title']=='ML Engineer']
chuong2=ch.loc[ch['job_title']=='Applied Scientist']
#tính tỷ lệ phần trăm cho mỗi nhóm
sizes=[len(chuong),len(chuong1),len(chuong2)]
# biểu đồ hình tròn phần trăm công việc
my_explode = (0.1,0,0)
my_colors = ['red','orange','silver',]
plt.pie(sizes,labels=['Data Scientist','ML Engineer','Applied Scientist'], explode=my_explode, colors=my_colors, autopct='%.1f%%')
plt.title('Phân bố các vị trí công việc')
plt.show()
#vẽ biểu đồ tròn 
plt.hist(tan_so,bins=500000)
plt.title("mức doanh thu của nhân viên")
plt.suptitle("phân bố")
plt.xlabel('mức lương')
plt.ylabel('số lượng')
plt.axis('equal')
plt.show()
#biểu đồ quy mô các công ty
my_colors = ['lightblue','lightsteelblue','silver']
my_explode = (0, 0.1, 0)
plt.pie(tan_so1,labels=dieu_kien1,autopct="%.1f%%",startangle=15,shadow=True,colors=my_colors,explode=my_explode)
plt.title("phân bố quy mô công ty")
plt.axis('equal')
plt.show()
# đổi kiểu dữ liệu của cột'salary' thành str
ch["salary"]=ch["salary"].astype(str)
# Vẽ biểu đồ cột
plt.hist(ch['salary'], bins=100)
plt.title("Mức doanh thu của nhân viên")
plt.xlabel("Mức lương")
plt.ylabel("Số lượng nhân viên")
plt.show()