def longest_overlap(word1, word2):
    n, m = len(word1), len(word2)

    max_overlap = -0x3f3f3f3f
    for i in range(n):
       for j in range(m):
           if word1[i] == word2[j]:
               catch_i, catch_j, count = i, j, 0
               while i < n and j < m and word1[i] == word2[j]:
                   i, j, count = i + 1, j + 1, count + 1
                
               i, j = catch_i, catch_j

               max_overlap = max(max_overlap, count)

    return max_overlap


print(longest_overlap("hello", "trello"))

