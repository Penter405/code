#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = malloc(2 * sizeof(int));

    int hash[numsSize];   // 不需要 numsSize+1
    int hashSize = 0;

    for (int x = 0; x < numsSize; x++) {
        for (int y = 0; y < hashSize; y++) {
            if (hash[y] == nums[x]) {
                result[0] = y;
                result[1] = x;
                *returnSize = 2;
                return result;
            }
        }
        hash[hashSize] = target - nums[x];
        hashSize++;
    }

    // 找不到答案
    result[0] = -1;
    result[1] = -1;
    *returnSize = 0;
    return result;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int* nums = a;
    int numSize = 5;
    int target = 7;

    int returnSize;
    int* ans = twoSum(nums, numSize, target, &returnSize);

    printf("%d %d\n", ans[0], ans[1]);

    free(ans);
    return 0;
}
