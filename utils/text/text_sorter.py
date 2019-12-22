import sys

input_path = sys.argv[1]
output_path = sys.argv[2]


def get_first_layer(string):
    return string[0]
    # regular_expression = "\w+"
    # return re.search(regular_expression, string)


with open(input_path) as f:
    content = f.readlines()

content = sorted(content, key=get_first_layer)

new = open(output_path, 'w')
for line in content:
    new.write("%s" % line)
