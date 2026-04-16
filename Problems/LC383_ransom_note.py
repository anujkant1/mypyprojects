"""
https://leetcode.com/problems/ransom-note/description/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
ransomNote = "alpha"
magazine = "alphanumeric"

def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_map = {}
    
    if len(ransomNote) > len(magazine):
        return False
    for item in magazine:
        if item not in mag_map:
            mag_map[item] = 1
        else:
            mag_map[item] += 1
    for item in ransomNote:
        if item in mag_map.keys():
            mag_map[item] -= 1
        else:
            return False
    return True

print(canConstruct(ransomNote, magazine))

