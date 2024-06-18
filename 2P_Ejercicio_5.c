#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 1000

// Función para inicializar matrices dispersas
void inicializar_matriz(int **matriz, int size, int densidad) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (rand() % 100 < densidad) {
                matriz[i][j] = rand() % 10 + 1;
            } else {
                matriz[i][j] = 0;
            }
        }
    }
}

// Función para multiplicar matrices con OpenMP
void multiplicar_matrices(int **A, int **B, int **C, int size) {
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            C[i][j] = 0;
            for (int k = 0; k < size; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    // Reservar memoria para las matrices
    int **matriz1 = malloc(N * sizeof(int *));
    int **matriz2 = malloc(N * sizeof(int *));
    int **resultado = malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        matriz1[i] = malloc(N * sizeof(int));
        matriz2[i] = malloc(N * sizeof(int));
        resultado[i] = malloc(N * sizeof(int));
    }
    // Inicializar matrices con una densidad del 10%
    inicializar_matriz(matriz1, N, 10);
    inicializar_matriz(matriz2, N, 10);

    // Multiplicar matrices con OpenMP
    multiplicar_matrices(matriz1, matriz2, resultado, N);

    // Imprimir una parte del resultado
    printf("Parte del resultado de la multiplicación:\n");
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", resultado[i][j]);
        }
        printf("\n");
    }
    // Liberar memoria
    for (int i = 0; i < N; i++) {
        free(matriz1[i]);
        free(matriz2[i]);
        free(resultado[i]);
    }
    free(matriz1);
    free(matriz2);
    free(resultado);

    return 0;
}







