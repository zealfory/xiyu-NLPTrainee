# Method 1
def replaceSpace(s):
	""" 
	: para s: str -- 字符串
	: return: str -- 替换后字符串
	"""
	return s.replace(' ', '%20')

# Method 2
def replace1(s):
    s_new = ""
    for i in range(len(s)):
        if s[i] == " ":
            s_new += "%20"
        else:
            s_new += s[i]
    return s_new


def main():
	s1 = "We Are Happy."
	print(replaceSpace(s1))
	print(replace1(s1))

if __name__ == "__main__":
	main() 
			 