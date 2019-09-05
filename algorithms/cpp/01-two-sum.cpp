/// Source: https://leetcode.com/problems/two-sum/
/// Author: Shun Kakinoki
/// Date: 2019-09-04

/* Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
 */

#include <bits/stdc++.h>
using namespace std;

#include <unordered_map>

class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        unordered_map<int, int> m;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++)
        {
            if (m.find(numbers[i]) == m.end())
            {
                m[target - numbers[i]] = i;
            }
            else
            {
                result.push_back(m[numbers[i]] + 1);
                result.push_back(i + 1);
                break;
            }
        }
        return result;
    }
};

int main()
{
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    Solution solution;
    vector<int> answer = solution.twoSum(numbers, target);
    cout << answer << endl;
    return 0;
}