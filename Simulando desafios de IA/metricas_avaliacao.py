n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))
  
def calculate_accuracy_precision(matrix):
    tp, fp, fn, tn = map(int, matrix)
    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) != 0 else 0 # Tratamento de 0
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0 # Tratamento de 0
    return accuracy, precision

def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    for index, matrix in enumerate(matrices):
        accuracy, precision = calculate_accuracy_precision(matrix)
        if (accuracy > best_accuracy) or (accuracy == best_accuracy and precision > best_precision):
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
    return best_index, best_accuracy, best_precision

best_index, best_accuracy, best_precision = best_performance(matrices)
# Print the results
print(f"Índice: {best_index + 1}")
print(f"Acurácia: {best_accuracy:.2f}")
print(f"Precisão: {best_precision:.2f}")