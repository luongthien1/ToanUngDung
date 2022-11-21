import numpy as np
import PPDon

#Kiểm tra xem có phải là chính tắc chưa, đánh dấu những phương trình chưa đáp ứng điều kiện
def KTCT(hpt : np.ndarray):
    m,n = hpt.shape
    dem2 = np.zeros((1,m))
    for i in range(n):
        dem = 0
        for j in range(m):
            if hpt[j][i] == 1:
                dem += 1
                mark = j
                if dem >1:
                    break
            elif hpt[j][i] != 0:
                break
            if (j==m-1)&(dem==1):
                dem2[0,mark] += 1
    return dem2

def PPMlon(fD:np.ndarray, hpt : np.ndarray, B:np.ndarray, vitri: np.ndarray, note: tuple[str,int] | None):
    m,n = hpt.shape
    theman = list()
    #Thêm ẩn với hệ số M lớn.
    for i in range(m):
        if vitri[0,i] == 1:
            continue
        elif vitri[0,i] == 0:
            theman.append(n+i-1)
            fD = np.hstack((fD,np.array(PPDon.M)))

            them = np.zeros((m,1))
            them[i,0] = 1.0
            hpt = np.hstack((hpt,them))
    hpt = np.hstack((hpt,B))

    notification,rs = PPDon.SimpleMethod(hpt,fD)[0:2]
    for i in range(len(theman)-1,0,-1):
        if rs[theman[i]] != 0.0:
            notification = "Phuong trinh vo nghiem"
            return notification,rs
    rs = rs[0:len(rs)-len(theman)]
    rs = rs[0:len(rs) - note[1]]
    return notification,rs
    


if __name__ == "__main__":
    fD,hpt,B,note = PPDon.read("inputM.txt")

    notification,rs = PPMlon(fD, hpt, B, KTCT(hpt), note)

    print(notification)
    print(rs)


