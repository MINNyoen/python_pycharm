# set (집합)
# 중복을 허용하지 않음.

score_list = [100, 30, 50, 60, 30, 100]
score_set = set(score_list)
type(score_set)
print(score_set)

score_list2 = [50, 60, 30, 100]
score_set2 = set(score_list2)
result = score_set2.intersection(score_set)
print(result)