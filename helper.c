#include <stdio.h>
#include <stdlib.h>

float *memorySimulator(int size, float startValue) {
    float *array = (float *)malloc(size * sizeof(float));
    if (array == NULL) {
        return NULL;
    }

    for (int index = 0; index < size; index++) {
        array[index] = startValue;
        startValue++;
    }

    return array;
}