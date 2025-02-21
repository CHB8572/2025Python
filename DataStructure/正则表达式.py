# 作者：乾
# 时间：2025年02月20日
# Mail:chb8572@gamil.com
import re


def match_rule():
    """
    正则表达式匹配
    """
    # 匹配以0-99的数字
    result = re.match(r"[1-9]?\d$", "0")
    print(result.group())
    print("-" * 50)
    # 匹配以1-99的数字
    try:
        result = re.match(r"^(?:[1-9]|[1-9][0-9])$", "99")  # ^匹配字符串的开始，$匹配字符串的结束 (?:)非捕获分组 | 或 [1-9] 1-9 [1-9][0-9]
        # 10-99
        print(result.group())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    match_rule()
    pass
