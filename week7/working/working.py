import re
import sys


def main():
    """转换时间而无需导入像 datetime 这样的库。"""
    print(convert(input("输入工作时间段：").strip()))


def convert(s):
    """将 12 小时制的时间转换为 24 小时制。"""
    work_times = []
    work_hours = []

    try:

        # 尝试在句子中查找所有工作时间。
        work_times = re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b", s, re.IGNORECASE)

        # 确保只提供了两个时间值
        if len(work_times) > 2 or len(work_times) < 2:
            raise ValueError

        for wt in work_times:

            # 检查是否为上午
            if " am" in str(wt).lower():
                wt = str(wt).lower().strip(" am")

                # 检查提供的时间是否为 12 小时制复杂时间。
                if has_minutes := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", wt):

                    # 检查值是否越界
                    if int(has_minutes.group(1)) > 12 or int(has_minutes.group(1)) < 1:
                        raise ValueError

                    elif int(has_minutes.group(1)) == 12:
                        work_hours.append(f"00:{has_minutes.group(2)}")

                    elif int(has_minutes.group(1)) <= 9:
                        work_hours.append(
                            f"0{has_minutes.group(1)}:{has_minutes.group(2)}"
                        )

                    else:
                        work_hours.append(
                            f"{has_minutes.group(1)}:{has_minutes.group(2)}"
                        )

                # 否则检查提供的时间是否为 12 小时制简单时间。
                elif has_hours := re.match(r"^(1[0-2]|0?[1-9])", wt):

                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError

                    elif int(has_hours.group(1)) == 12:
                        work_hours.append(f"00:00")

                    elif int(has_hours.group(1)) <= 9:
                        work_hours.append(f"0{has_hours.group(1)}:00")

                    else:
                        work_hours.append(f"{has_hours.group(1)}:00")

                else:
                    raise ValueError

            # 检查是否为下午
            if " pm" in str(wt).lower():
                wt = str(wt).lower().strip(" pm")

                # 检查提供的时间是否为 12 小时制复杂时间。
                if has_minutes := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", wt):

                    if int(has_minutes.group(1)) > 12 or int(has_minutes.group(1)) < 1:
                        raise ValueError

                    elif int(has_minutes.group(1)) == 12:
                        work_hours.append(f"12:{has_minutes.group(2)}")

                    else:
                        work_hours.append(
                            f"{int(has_minutes.group(1)) + 12}:{has_minutes.group(2)}"
                        )

                # 否则检查提供的时间是否为 12 小时制简单时间。
                elif has_hours := re.match(r"^(1[0-2]|0?[1-9])", wt):

                    # 检查值是否越界
                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError

                    elif int(has_hours.group(1)) == 12:
                        work_hours.append(f"12:00")

                    else:
                        work_hours.append(f"{int(has_hours.group(1)) + 12}:00")

                else:
                    raise ValueError

    except ValueError:
        raise ValueError

    # 确保有两个值可以返回
    if len(work_hours) == 2:
        return f"{work_hours[0]} to {work_hours[1]}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
