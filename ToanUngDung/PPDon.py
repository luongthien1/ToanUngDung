import numpy as np
import io
M= 100000.00

def readnext(f:io.TextIOWrapper):
    # đọc từ tiếp theo, bỏ qua dấu ký tự trống
    s=""
    while(f.readable()):
        s = f.read(1)
        if (s == " ") or (s == "\n"):
            continue
        else:
            break
    while(f.readable()):
        t = f.read(1)
        if (t == " ") or (t == "\n") or (t==""):
            break
        s += t
    return s


#phương pháp đơn hình
def SimpleMethod(array: np.ndarray, f: np.ndarray):
    m=len(array)
    table = list(list())

    #Chuyển B về đầu của table
    for i in range(m):
        l = list()
        l.append(array[i][-1])
        l=np.hstack((l,array[i][0:len(f)]))
        table.append(l)
    AnCB = list()

    #Xác định ẩn cơ bản
    for j in range(len(f)):
        has = False
        for i in range(m):
            if (array[i][j]!=1.0) & (array[i][j]!=0.0):
                break
            elif array[i][j]==1:
                if has:
                    break
                else:
                    has = True
            if i== m-1:
                AnCB.append(j+1)

    #Tính hàng delta và thêm vào table   
    f = np.hstack(([0],f))
    ldelta = list()
    for i in range(len(f)):
        delta = 0
        for j in range(m):
            delta+=table[j][i]*f[AnCB[j]]
        delta -= f[i]
        ldelta.append(delta)
    table.append(ldelta)

    #Khởi tạo hàng quay, kiểm tra tính tối ưu
    hangquay = -1
    check = ""
    check = toiuu(table)

    #Khi vẫn chưa đạt tính tối ưu nhưng không vô nghiệm, tính ...
    while (check=="CN"):
        #Xác định cột quay bằng cách lấy max của hàng delta(hàng cuối của table), loại trừ phần từ đầu tiên
        cotquay = table[-1].index(max(table[-1][1:len(table[-1])]))
        #Xác định cột chia, tìm hàng quay = hàng của phần tử nhỏ nhất trong cột chia
        chia = list()
        for i in range(m):
            if (hangquay == i):
                chia.append(M)
                continue
            chia.append(table[i][0]/table[i][cotquay])
        hangquay = chia.index(min(chia))
        # Đổi ẩn cơ bản
        AnCB[hangquay] = cotquay
        # Xác định tâm quay
        tam = table[hangquay][cotquay]
        #Tạo bảng sao table, dựa vào đó cập nhật table
        table2 = np.array(table)
        for i in range(len(f)):
            for j in range(m+1):
                if j==hangquay:
                    table[j][i] /=tam
                elif i==cotquay:
                    table[j][i] = 0
                else:
                    table[j][i] -= table2[hangquay][i]*table2[j][cotquay]/tam
        print("tam = a"+str(hangquay)+str(cotquay)+" = "+str(tam)+"\n")
        print(np.array(table))
        #kiểm tra lại tính tối ưu
        check = toiuu(table)
    # nếu tính tối ưu
    if check=="TU":
        # Các ẩn được khởi tạo có giá trị 0
        dapan = np.zeros_like(np.arange(len(f)), dtype=float)
        # Các ẩn là ẩn cơ bản cuối cùng có giá trị bằng cột đầu tiên của table(cột P/Án)
        for i in range(len(AnCB)):
            dapan[AnCB[i]] = table[i][0]
        dapan = dapan[1:len(dapan)]
        return "f(x)min = "+str(table[-1][0]),dapan,table
    else:
        return "phương trình vô nghiệm","  ",table
    

def toiuu(table : list[list]):
    rowd = table[len(table) - 1]
    store = list()
    for i in range(1,len(rowd)):
        if rowd[i]>0:
            store.append(i)
    if len(store) >0:
        for i in store:
            dem = 0
            for j in range(len(table)-1):
                if table[j][i]<0:
                    dem+=1
            if dem == len(table)-1:
                return "VO"
        return "CN"
    return "TU"

def read(path:str):
    #lấy dữ liệu vào f(x,D)
    fD = list()
    f = io.open(path, mode = "r")
    n = int(readnext(f))
    for i in range(n):
        c = readnext(f)
        fD.append(float(c))
    fD = np.array(fD)
    n0 = fD.shape[0]
    mode = readnext(f)
    if mode.upper() == "MAX":
        fD *=-1
    
    #lấy dữ liệu vào hệ phương trình
    m = int(readnext(f))
    hpt = np.zeros_like(np.arange(m*n).reshape(m,n),dtype=float)
    dau = list()
    B = np.zeros_like(np.arange(m).reshape(m,1))
    for i in range(m):
        for j in range(n):
            hpt[i][j] = float(readnext(f))
        dau.append(readnext(f))
        B[i] = float(readnext(f))

        if B[i] < 0:
            hpt[i] = hpt[i] *(-1)
            B[i] *= -1

        # Đặt ẩn phụ
        if dau[-1] != "=":
            if (dau[-1] == ">=") or (dau[-1] ==">"): 
                Aadd = np.zeros_like(np.arange(m).reshape(m,1))
                Aadd[i] = -1
            if (dau[-1] == "<=") or (dau[-1] =="<"): 
                Aadd = np.zeros_like(np.arange(m).reshape(m,1))
                Aadd[i] = 1
            hpt = np.hstack((hpt,Aadd))
            fD = np.append(fD,0)
    n=fD.shape[0]
    B = np.array(B)
    #Số ẩn phụ sử dụng
    SoAnPhu = n-n0
    return fD,hpt,B,(mode,SoAnPhu)

if __name__ == "__main__":
    fD,hpt,B,tuychinh = read("inputDon.txt")
    hpt = np.hstack((hpt,B))
    fmin,rs, = SimpleMethod(hpt,fD)[0:2]
    print(fmin)
    print(rs)

    



