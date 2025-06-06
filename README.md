# task8_karthikeyan
# 🧠 K-Means Clustering (No Sklearn)

This project implements the **K-Means Clustering Algorithm** from scratch using **only NumPy, Matplotlib, and basic Python** — without relying on external machine learning libraries like `sklearn`.

---

## 🚀 Features

- ✅ Custom implementation of K-Means algorithm.
- ✅ Visualizes clusters and centroids with `matplotlib`.
- ✅ Automatically handles empty clusters.
- ✅ No dependency on `sklearn`.

---

## 📊 Dataset Used
**Mall_Customers.csv**

Features used:
- `Annual Income (k$)`
- `Spending Score (1-100)`

---

## 🧰 Packages Used

```bash
## 🧑‍💻 How It Works

1. **Initialization**:
   - Randomly selects `k` data points as initial centroids.

2. **Assignment Step**:
   - Assigns each data point to the nearest centroid using Euclidean distance.

3. **Update Step**:
   - Recalculates centroids by averaging the points in each cluster.

4. **Repeat**:
   - Continues until centroids do not change (convergence) or max iterations are reached.

5. **Plotting**:
   - Uses `matplotlib` to display the clustered data points and centroids.

---

## 🛠️ How to Run

### 🔧 Requirements

Make sure you have Python installed. You can install the required packages using:

```bash
pip install numpy matplotlib


****** output 

![image](https://github.com/user-attachments/assets/29e2c6da-c6c8-46bc-a8c6-7a437ffbb499)

