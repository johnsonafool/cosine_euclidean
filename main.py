from scipy.spatial import distance

# case one
O = [0.00, 0.00]
A = [1.45, 7.56]
B = [7.81, 12.41]
C = [8.83, 4.48]


euc_dstA_B = distance.euclidean(A,B)
euc_dstB_C = distance.euclidean(B,C)
euc_dstA_C = distance.euclidean(C,A)

cos_simA_B = 1 - distance.cosine(A, B)
cos_simB_C = 1 - distance.cosine(B, C)
cos_simA_C = 1 - distance.cosine(A, C)

# print("e_AC, e_BC, e_AC")
# print(euc_dstA_B, euc_dstB_C, euc_dstA_C)
# print()
# print("c_AC, c_BC, c_AC")
# print(cos_simA_B, cos_simB_C, cos_simA_C)

# case two
A_ = [8.00, 2.00]
B_ = [12.00, 3.00]
C_ = [32.00, 8.00]

cos_simA_B_ = 1 - distance.cosine(A_, B_)
cos_simB_C_ = 1 - distance.cosine(B_, C_)
cos_simA_C_ = 1 - distance.cosine(A_, C_)

dstA_B_ = distance.euclidean(A_,B_)
dstB_C_ = distance.euclidean(B_,C_)
dstA_C_ = distance.euclidean(C_,A_)
