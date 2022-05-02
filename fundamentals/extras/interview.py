def solution(input, target_word):
    # Please write your code here.
    count = input.count(target_word)
    for i in input:
        if i == target_word:
            print(count)
    return count

print(solution("foo bar", "foo"))


