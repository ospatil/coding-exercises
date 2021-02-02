def reverse(str):
    if len(str) <= 1:
        return str
    return reverse(str[1:]) + str[0]


if __name__ == "__main__":
    str = "omkar"
    print(f"reverse {str} = {reverse(str)}")
