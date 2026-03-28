import math

# 1. Dataset sederhana (fitur + label)
dataset = [
    [1, 1, 'A'],
    [2, 2, 'A'],
    [8, 8, 'B'],
    [9, 9, 'B']
]

# 2. Hitung jarak Euclidean
def euclidean_distance(p1, p2):
    distance = 0
    for i in range(len(p2)-1):  # -1 karena kolom terakhir adalah label
        distance += (p1[i] - p2[i]) ** 2 #untuk menghasilkan jarak dari x dan y dijumlahkan, dikuadratkan dann akar seperti pythagoras
    return math.sqrt(distance) 

# 3. Cari K tetangga terdekat
def get_neighbors(dataset, test_point, k):
    distances = []

    for data in dataset:
        dist = euclidean_distance(test_point, data)
        distances.append((data, dist))

    # urutkan berdasarkan jarak
    distances.sort(key=lambda x: x[1]) #lambda untuk menggunaakan penyortiran hanya berdasarkan 1 variabel saja dan x[1] adalah dist

    # ambil K terdekat
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0]) #pembuatan list baru berisi data jarak yang terurut

    return neighbors #menjadi list yang sudah terurut jaraknya

# 4. Voting (tentukan kelas)
def predict_class(neighbors):
    votes = {} #urutkan menggunakan dict dengan key label dan item adalah jumlah tetangga

    for neighbor in neighbors:
        label = neighbor[-1]  # ambil label
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    # cari label dengan vote terbanyak
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True) #reverse urutkan dari besar ke kecil
    return sorted_votes[0][0] #ambil yang terbesar

# 5. Testing
test_point = [3, 3]  # data baru
k = 3

neighbors = get_neighbors(dataset, test_point, k)
result = predict_class(neighbors)

print("Tetangga terdekat:", neighbors)
print("Prediksi:", result)