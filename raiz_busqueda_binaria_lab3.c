#include <stdio.h>
#include <stdlib.h>

int raizCuadradaBusquedaBinaria(int X) {
    if (X == 0 || X == 1) {
        return X;
    }

    int l = 0;
    int r = X / 2;
    int ans;

    while (l <= r) {
        int mitad = (l + r) / 2;
        int cuadradoMitad = mitad * mitad;

        if (cuadradoMitad == X) {
            return mitad;
        } else if (cuadradoMitad < X) {
            l = mitad + 1;
            ans = mitad;
        } else {
            r = mitad - 1;
        }
    }

    return ans;
}

int main() {
    int numero;
    printf("Ingrese el numero a buscar su raiz cuadrada: ");
    scanf("%d", &numero);
    printf("La raiz cuadrada de %d es %d\n", numero, raizCuadradaBusquedaBinaria(numero));
    return 0;
}