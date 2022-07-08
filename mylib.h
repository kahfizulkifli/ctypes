#pragma once
 
#ifdef __cplusplus
extern "C" {
#endif
 
void test_empty(void);
float test_add(float x, float y);
void test_passing_array(int *data, int len);
char* get_address();
 
#ifdef __cplusplus
}
#endif