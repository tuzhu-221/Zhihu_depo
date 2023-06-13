import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')
    parser.add_argument('--compress', action='store_true', help='Compress the image which is too large')
    parser.add_argument('-i', '--input', type=str, help='Path to the file you want to transfer.')
    parser.add_argument('-e', '--encoding', type=str, help='Encoding of the input file')

    args = parser.parse_args()
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        if args.encoding == None:
            args.encoding = "UTF-8"
        print(args.input)
        
        print(args.encoding)
        location = "D://blog/blog_new/source/_posts/" + args.input
        f = open(location,encoding=args.encoding)
        content = f.readlines()
        for i in range(len(content)):
            content[i] = re.sub('(\$)(?!\$)(.*?)(\$)', 
                        ' \\1\\1\\2\\1\\1 ',content[i])
        string = str()
        for i in content:
            string += i
        new_eq = r"""
\\begin{equation}
\\begin{aligned}
\2
\\end{aligned}
\\end{equation}
"""
        new_string = re.sub('(\n\$\$\n)([\s\S]*?)(\n\$\$\n)',new_eq,string)
        
        f.close()
        f = open("zhihu.md","w",encoding=args.encoding)
        f.write(new_string)
        f.close()
    