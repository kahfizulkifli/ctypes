#include <stdio.h>
#include "mylib.h"
#include <iostream>
#include <memory>

using namespace std;

void test_empty(void) {
    puts("Hello from C");
}

float test_add(float x, float y) {
    return x + y;
}

void test_passing_array(int *data, int len) {
    printf("Data as received from python\n");
    for(int i = 0; i < len; ++i) {
        printf("%d ", data[i]);
    }
    puts("");

    for (int i = 0; i < len; i++) {
        data[i] = -i;
    }
}

char * get_address() {
    char* test = "Hello world";
    return test;
}